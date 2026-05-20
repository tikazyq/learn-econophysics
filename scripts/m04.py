import matplotlib
matplotlib.use("Agg")
from pathlib import Path
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ASSETS = Path(__file__).resolve().parents[1] / "src" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

tickers = [
    "AAPL","MSFT","GOOGL","AMZN","META","TSLA","NVDA","JPM","JNJ","V",
    "PG","UNH","HD","MA","BAC","DIS","XOM","ABBV","KO","PEP",
    "MRK","CVX","WMT","PFE","CSCO","LLY","TMO","ABT","COST","AVGO",
    "MCD","ACN","DHR","NEE","NKE","WFC","TXN","CRM","ORCL","ADBE",
    "BMY","UNP","UPS","HON","RTX","QCOM","T","LOW","LIN","SBUX",
    "IBM","INTC","AMGN","GS","CAT","BLK","BA","MDT","C","AXP",
    "PM","SCHW","DE","ISRG","SPGI","MS","MMM","NOW","INTU","BKNG",
    "GE","CVS","TGT","ADP","PLD","AMT","MO","ZTS","TJX","CB",
    "DUK","CL","SO","SYK","BDX","LMT","CCI","MMC","ITW","COP",
    "MDLZ","AMD","ADI","GILD","REGN","ETN","BSX","EOG","FIS","CME",
]

px = yf.download(tickers, start="2020-01-01", end="2025-01-01", auto_adjust=True, progress=False)["Close"]
px = px.dropna(axis=1, thresh=int(0.95 * len(px)))
ret = np.log(px).diff().dropna()
N, T = ret.shape[1], ret.shape[0]
q = N / T
print(f"N={N}, T={T}, q={q:.3f}")

Z = (ret - ret.mean()) / ret.std()
C = (Z.T @ Z).values / T
eigvals = np.linalg.eigvalsh(C)

lam_minus = (1 - np.sqrt(q))**2
lam_plus  = (1 + np.sqrt(q))**2
lam_grid = np.linspace(lam_minus, lam_plus, 500)
mp_pdf = np.sqrt((lam_plus - lam_grid) * (lam_grid - lam_minus)) / (2 * np.pi * q * lam_grid)

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(eigvals, bins=50, density=True, alpha=0.6, label="empirical eigenvalues")
ax.plot(lam_grid, mp_pdf, "r-", lw=2, label=f"MP (q={q:.2f})")
ax.axvline(lam_plus, color="r", ls="--", alpha=0.5)
ax.set_xlabel(r"$\lambda$"); ax.set_ylabel("density")
ax.set_title("Eigenvalue spectrum vs Marchenko-Pastur")
ax.legend()

outliers = eigvals[eigvals > lam_plus]
print(f"#eigenvalues > lambda_+ = {len(outliers)} / {N}")
print(f"lambda_+ (MP upper edge) = {lam_plus:.3f}")
print(f"largest = {eigvals[-1]:.2f}  (market mode)")
print(f"top 5 eigenvalues: {np.round(eigvals[-5:][::-1], 2).tolist()}")

plt.savefig(ASSETS / "m04-mp-spectrum.png", dpi=110, bbox_inches="tight")
