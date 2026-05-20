"""Minimal heterogeneous-agent model: Cont-Bouchaud (2000) cluster herding.

N traders are grouped into clusters that merge stochastically. Each step, each
cluster decides as a group to buy, sell, or stay. Because cluster sizes
follow a power-law distribution under merge dynamics, the net order flow
inherits a heavy tail. The resulting return time series shows fat tails and
volatility clustering, both emerging from a single mechanism (correlated
decisions inside clusters).
"""

import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

T = 5000
N = 500             # number of traders
a = 0.30            # per-step probability a cluster is active (else holds)
p_merge = 0.0003    # per-pair merge rate per step
p_split = 0.40      # cluster dissolution rate per step
lam = 0.01          # price impact per net order
p_star = 100.0
p = np.zeros(T); p[0] = p_star
fund_pull = 0.001   # mild mean-reversion to fundamental

# Initialize: each trader is its own cluster
cluster_of = np.arange(N)

def cluster_sizes(cluster_of):
    sizes = np.bincount(cluster_of)
    return sizes[sizes > 0]

active_size_frac = np.zeros(T)
biggest_cluster = np.zeros(T, dtype=int)

for t in range(1, T):
    # 1) Random merges: pick a few pairs
    n_merge_trials = max(1, int(p_merge * N * N))
    for _ in range(n_merge_trials):
        i, j = np.random.randint(0, N, 2)
        ci, cj = cluster_of[i], cluster_of[j]
        if ci != cj:
            # merge into min label
            new, old = (ci, cj) if ci < cj else (cj, ci)
            cluster_of[cluster_of == old] = new

    # 2) Random splits: each cluster dissolves with prob p_split
    labels = np.unique(cluster_of)
    for c in labels:
        if np.random.rand() < p_split:
            members = np.where(cluster_of == c)[0]
            cluster_of[members] = members  # each trader becomes own cluster

    # 3) Trading decisions: each cluster picks (-1, 0, +1) with prob (a/2, 1-a, a/2)
    labels = np.unique(cluster_of)
    net = 0.0
    active_pop = 0
    for c in labels:
        u = np.random.rand()
        if u < a / 2:
            decision = -1
        elif u < a:
            decision = +1
        else:
            decision = 0
        if decision != 0:
            size = np.sum(cluster_of == c)
            net += decision * size
            active_pop += size

    # 4) Price update: impact + mild fundamental pull
    drift = -fund_pull * np.log(p[t-1] / p_star)
    r_t = lam * net / N + drift
    p[t] = p[t-1] * np.exp(r_t)
    active_size_frac[t] = active_pop / N
    biggest_cluster[t] = max(cluster_sizes(cluster_of))

r = np.diff(np.log(p))

fig, axes = plt.subplots(2, 2, figsize=(13, 10))
axes[0, 0].plot(p, lw=0.8)
axes[0, 0].axhline(p_star, color="r", ls="--", label=r"$p^*$")
axes[0, 0].set_title("Price path")
axes[0, 0].legend()

axes[0, 1].plot(biggest_cluster, lw=0.6)
axes[0, 1].set_title("Largest cluster size")

axes[1, 0].hist(r, bins=80, density=True, alpha=0.7, label="empirical")
from scipy import stats
mu, sd = r.mean(), r.std()
xs = np.linspace(r.min(), r.max(), 200)
axes[1, 0].plot(xs, stats.norm.pdf(xs, mu, sd), "r-", lw=2,
                label=r"$\mathcal{N}(\mu, \sigma^2)$")
axes[1, 0].set_yscale("log")
axes[1, 0].legend()
axes[1, 0].set_title("Return distribution (log)")

from statsmodels.tsa.stattools import acf
lags = np.arange(1, 201)
acf_abs = acf(np.abs(r), nlags=200, fft=True)[1:]
axes[1, 1].loglog(lags, np.maximum(acf_abs, 1e-4), "k.")
axes[1, 1].set_title(r"ACF of $|r|$")

plt.tight_layout()
plt.savefig("/home/user/learn-econophysics/src/assets/m07-heterogeneous-agents.png",
            dpi=110, bbox_inches="tight")

print(f"price: min = {p.min():.2f}, max = {p.max():.2f}, mean = {p.mean():.2f}")
print(f"largest cluster: time mean = {biggest_cluster.mean():.1f}, max = {biggest_cluster.max()}")
print(f"return: std = {r.std():.5f}, kurtosis = {stats.kurtosis(r):.2f}")
print(f"ACF(|r|) at lag 1, 10, 50, 100 = "
      f"{acf_abs[0]:.3f}, {acf_abs[9]:.3f}, {acf_abs[49]:.3f}, {acf_abs[99]:.3f}")
