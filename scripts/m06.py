import matplotlib
matplotlib.use("Agg")
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

ASSETS = Path(__file__).resolve().parents[1] / "src" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


class LOB:
    def __init__(self, mid=100.0, tick=0.01, depth_init=5):
        self.tick = tick
        self.bids = defaultdict(int)
        self.asks = defaultdict(int)
        for k in range(1, 30):
            self.bids[round(mid - k*tick, 2)] = depth_init
            self.asks[round(mid + k*tick, 2)] = depth_init

    def best_bid(self):
        return max(self.bids) if self.bids else None

    def best_ask(self):
        return min(self.asks) if self.asks else None

    def mid(self):
        b, a = self.best_bid(), self.best_ask()
        if b is None or a is None:
            return self._last_mid if hasattr(self, "_last_mid") else 100.0
        self._last_mid = 0.5 * (b + a)
        return self._last_mid

    def submit_limit(self, side, price):
        book = self.bids if side == "buy" else self.asks
        book[round(price, 2)] += 1

    def submit_market(self, side, size=1):
        # Walk the book up to `size` shares, returning the volume-weighted price.
        traded = 0
        notional = 0.0
        if side == "buy":
            while traded < size and self.asks:
                p = min(self.asks)
                take = min(size - traded, self.asks[p])
                self.asks[p] -= take
                if self.asks[p] == 0:
                    del self.asks[p]
                notional += take * p
                traded += take
        else:
            while traded < size and self.bids:
                p = max(self.bids)
                take = min(size - traded, self.bids[p])
                self.bids[p] -= take
                if self.bids[p] == 0:
                    del self.bids[p]
                notional += take * p
                traded += take
        return notional / traded if traded > 0 else None

    def cancel(self, side):
        book = self.bids if side == "buy" else self.asks
        if not book:
            return
        prices = list(book.keys())
        p = np.random.choice(prices)
        book[p] -= 1
        if book[p] == 0:
            del book[p]


np.random.seed(0)
lob = LOB()
mids, trades = [], []
rate_limit, rate_market, rate_cancel = 0.55, 0.20, 0.25

for t in range(50000):
    side = np.random.choice(["buy", "sell"])
    u = np.random.rand()
    if u < rate_limit:
        # Limit orders are placed at the same-side touch and shifted up to 4 ticks
        # toward the opposite side (i.e. into the spread), then clamped to one
        # tick inside the opposite touch so they don't cross the book.
        offset = np.random.choice([0, 0, 1, 2, 3, 4]) * lob.tick
        ref = lob.best_bid() if side == "buy" else lob.best_ask()
        if ref is None:
            ref = lob.mid()
        price = (ref + offset) if side == "buy" else (ref - offset)
        opp = lob.best_ask() if side == "buy" else lob.best_bid()
        if opp is not None:
            if side == "buy" and price >= opp:
                price = opp - lob.tick
            if side == "sell" and price <= opp:
                price = opp + lob.tick
        lob.submit_limit(side, price)
    elif u < rate_limit + rate_market:
        # Variable-sized market orders: occasional bursts walk multiple levels
        size = int(np.random.choice([1, 1, 2, 3, 5], p=[0.45, 0.25, 0.15, 0.10, 0.05]))
        p = lob.submit_market(side, size=size)
        if p is not None:
            trades.append((t, p, side, size))
    else:
        lob.cancel(side)
    mids.append(lob.mid())

mids = np.array(mids)

# Aggregate to bars so per-bar returns mix many micro-events
bar = 50
mid_bar = mids[bar - 1::bar]
r = np.diff(np.log(mid_bar))

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
axes[0].plot(mids, lw=0.5)
axes[0].set_title("Mid-price path (tick by tick)")
axes[1].hist(r, bins=60, density=True, alpha=0.7, label="bar returns")
# Overlay a Gaussian fitted to the same std for visual comparison
from scipy import stats
mu, sd = r.mean(), r.std()
xs = np.linspace(r.min(), r.max(), 200)
axes[1].plot(xs, stats.norm.pdf(xs, mu, sd), "r-", lw=2, label=r"$\mathcal{N}(\mu, \sigma^2)$")
axes[1].set_yscale("log")
axes[1].legend()
axes[1].set_title(f"Return distribution at {bar}-step bars")

from statsmodels.tsa.stattools import acf
acf_abs = acf(np.abs(r), nlags=100, fft=True)[1:]
lags_plot = np.arange(1, 101)
axes[2].loglog(lags_plot, np.maximum(acf_abs, 1e-4), "k.")
axes[2].set_title(r"ACF of $|r|$ (log-log)")
axes[2].set_xlabel("lag")
axes[2].set_ylabel(r"$\rho_{|r|}$")

plt.tight_layout()
plt.savefig(ASSETS / "m06-zero-intel-lob.png", dpi=110, bbox_inches="tight")

print(f"#trades = {len(trades)} / {len(mids)} steps; #bars = {len(mid_bar)}")
print(f"mid: min = {mids.min():.3f}, max = {mids.max():.3f}, "
      f"range = {mids.max() - mids.min():.3f}")
print(f"bar return: std = {r.std():.5f}, kurtosis = {stats.kurtosis(r):.2f}")
print(f"ACF(|r|) at lag 1, 5, 20, 50 = "
      f"{acf_abs[0]:.3f}, {acf_abs[4]:.3f}, {acf_abs[19]:.3f}, {acf_abs[49]:.3f}")
