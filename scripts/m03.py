import matplotlib
matplotlib.use("Agg")
from pathlib import Path
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

ASSETS = Path(__file__).resolve().parents[1] / "src" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

spx = yf.download("^GSPC", start="2005-01-01", end="2025-01-01", auto_adjust=True, progress=False)
r = np.log(spx["Close"]).diff().dropna().values.flatten()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

plot_acf(r, lags=60, ax=axes[0], title=r"ACF of $r_t$")
plot_acf(np.abs(r), lags=60, ax=axes[1], title=r"ACF of $|r_t|$")

from statsmodels.tsa.stattools import acf
lags = np.arange(1, 250)
acf_abs = acf(np.abs(r), nlags=lags.max(), fft=True)[1:]
mask = acf_abs > 0
axes[2].loglog(lags[mask], acf_abs[mask], "k.", ms=4)
axes[2].set_xlabel(r"lag $\tau$ (days)")
axes[2].set_ylabel(r"$\rho_{|r|}(\tau)$")
axes[2].set_title("Power-law decay of |r| ACF")

slope, intercept = np.polyfit(np.log(lags[mask][:100]), np.log(acf_abs[mask][:100]), 1)
print(f"Estimated decay exponent gamma = {-slope:.2f}")

acf_r = acf(r, nlags=60, fft=True)
print(f"ACF(r) at lag 1, 2, 3 = {acf_r[1]:.3f}, {acf_r[2]:.3f}, {acf_r[3]:.3f}")
print(f"ACF(|r|) at lag 1, 10, 60 = {acf_abs[0]:.3f}, {acf_abs[9]:.3f}, {acf_abs[59]:.3f}")

plt.tight_layout()
plt.savefig(ASSETS / "m03-vol-clustering.png", dpi=110, bbox_inches="tight")
