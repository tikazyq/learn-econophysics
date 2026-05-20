import matplotlib
matplotlib.use("Agg")
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy import stats

spx = yf.download("^GSPC", start="2005-01-01", end="2025-01-01", auto_adjust=True, progress=False)
returns = np.log(spx["Close"]).diff().dropna().values.flatten()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
mu, sigma = returns.mean(), returns.std()
x = np.linspace(returns.min(), returns.max(), 500)

axes[0].hist(returns, bins=200, density=True, alpha=0.6, label="empirical")
axes[0].plot(x, stats.norm.pdf(x, mu, sigma), "r-", lw=2, label=r"$\mathcal{N}(\mu, \sigma^2)$")
axes[0].set_yscale("log")
axes[0].set_title("S&P 500 daily log-returns vs Gaussian")
axes[0].set_xlabel("log-return"); axes[0].set_ylabel("density (log)")
axes[0].legend()

stats.probplot(returns, dist="norm", plot=axes[1])
axes[1].set_title("Q-Q plot against normal")

plt.tight_layout()
plt.savefig("/home/user/learn-econophysics/src/assets/m01-gaussian-fails.png", dpi=110, bbox_inches="tight")
print(f"n_obs = {len(returns)}")
print(f"mu = {mu:.6f}, sigma = {sigma:.6f}")
print(f"min = {returns.min():.4f}, max = {returns.max():.4f}")
print(f"sample kurtosis = {stats.kurtosis(returns):.2f}  (Gaussian excess kurtosis = 0)")
print(f"#|r|>4σ = {(np.abs(returns) > 4*sigma).sum()}   "
      f"Gaussian expectation ≈ {len(returns)*2*(1-stats.norm.cdf(4)):.2f}")
