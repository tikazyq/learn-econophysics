import matplotlib
matplotlib.use("Agg")
from pathlib import Path
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

ASSETS = Path(__file__).resolve().parents[1] / "src" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

spx = yf.download("^GSPC", start="2005-01-01", end="2025-01-01", auto_adjust=True, progress=False)
returns = np.log(spx["Close"]).diff().dropna().values.flatten()

abs_r = np.abs(returns)
abs_r_sorted = np.sort(abs_r)[::-1]
n = len(abs_r_sorted)
ranks = np.arange(1, n + 1)
survival = ranks / n

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].loglog(abs_r_sorted, survival, "k.", ms=2)
axes[0].set_xlabel(r"$|r|$")
axes[0].set_ylabel(r"$P(|R| > |r|)$")
axes[0].set_title("Empirical survival function (log-log)")

def hill_estimator(sorted_desc, k):
    Xk1 = sorted_desc[k]
    return 1.0 / np.mean(np.log(sorted_desc[:k] / Xk1))

ks = np.arange(20, min(n // 20, 500))
hill = np.array([hill_estimator(abs_r_sorted, k) for k in ks])

axes[1].plot(ks, hill, "b-")
axes[1].axhline(3, color="r", ls="--", label=r"$\alpha=3$ (inverse cubic)")
axes[1].set_xlabel(r"$k$ (number of order stats used)")
axes[1].set_ylabel(r"$\hat\alpha_k^{Hill}$")
axes[1].set_title("Hill plot")
axes[1].legend()

import powerlaw
fit = powerlaw.Fit(abs_r, xmin=None, discrete=False, verbose=False)
alpha_hat = fit.power_law.alpha
xmin_hat = fit.power_law.xmin
print(f"Clauset MLE: alpha = {alpha_hat - 1:.2f}, xmin = {xmin_hat:.4f}")
fit.plot_pdf(ax=axes[2], color="k", marker=".", linestyle="None")
fit.power_law.plot_pdf(ax=axes[2], color="r", linestyle="--",
                       label=fr"power-law, $\alpha={alpha_hat-1:.2f}$")
axes[2].set_title("Clauset MLE fit")
axes[2].legend()

# Hill plateau report
plateau_mask = (ks >= 50) & (ks <= 500)
print(f"Hill plot plateau (k in [50, 500]): mean alpha ≈ {hill[plateau_mask].mean():.2f}, "
      f"std = {hill[plateau_mask].std():.2f}")

plt.tight_layout()
plt.savefig(ASSETS / "m02-power-law-alpha.png", dpi=110, bbox_inches="tight")
