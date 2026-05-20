import matplotlib
matplotlib.use("Agg")
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ASSETS = Path(__file__).resolve().parents[1] / "src" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

np.random.seed(42)

def metropolis_step(s, beta):
    L = s.shape[0]
    for _ in range(L * L):
        i, j = np.random.randint(0, L, size=2)
        nb = s[(i+1) % L, j] + s[i-1, j] + s[i, (j+1) % L] + s[i, j-1]
        dE = 2 * s[i, j] * nb
        if dE <= 0 or np.random.rand() < np.exp(-beta * dE):
            s[i, j] = -s[i, j]
    return s

L = 32
n_eq = 1000
n_meas = 3000
Ts = np.linspace(1.6, 3.2, 12)
Tc_theory = 2 / np.log(1 + np.sqrt(2))

m_mean, chi = [], []
for T in Ts:
    beta = 1.0 / T
    s = np.random.choice([-1, 1], size=(L, L))
    for _ in range(n_eq):
        metropolis_step(s, beta)
    m_abs_samples, m_sq_samples = [], []
    for _ in range(n_meas):
        metropolis_step(s, beta)
        m_inst = s.mean()
        m_abs_samples.append(abs(m_inst))
        m_sq_samples.append(m_inst * m_inst)
    m_abs_samples = np.array(m_abs_samples)
    m_sq_samples  = np.array(m_sq_samples)
    m_mean.append(m_abs_samples.mean())
    chi.append(beta * L * L * (m_sq_samples.mean() - m_abs_samples.mean()**2))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].plot(Ts, m_mean, "ko-")
axes[0].axvline(Tc_theory, color="r", ls="--", label=fr"$T_c \approx {Tc_theory:.2f}$")
axes[0].set_xlabel("T"); axes[0].set_ylabel(r"$|m|$"); axes[0].set_title("Magnetization")
axes[0].legend()

axes[1].plot(Ts, chi, "bo-")
axes[1].axvline(Tc_theory, color="r", ls="--")
axes[1].set_xlabel("T"); axes[1].set_ylabel(r"$\chi$"); axes[1].set_title("Susceptibility")

plt.tight_layout()
plt.savefig(ASSETS / "m05-ising-transition.png", dpi=110, bbox_inches="tight")

i_peak = int(np.argmax(chi))
print(f"Theoretical Tc = {Tc_theory:.3f}")
print(f"chi peaks at T = {Ts[i_peak]:.3f}, chi_max = {chi[i_peak]:.2f}")
print(f"|m| at T=1.6: {m_mean[0]:.3f}    |m| at T=3.2: {m_mean[-1]:.3f}")
