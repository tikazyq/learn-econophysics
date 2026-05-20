# Lab scripts

Each `mXX.py` is the runnable version of the Python lab in module `XX` of the
textbook. They generate the figures saved under `../src/assets/` and print
the numeric output that is embedded in each module's markdown.

The textbook embeds the figures and numbers directly, so readers do not need
to run anything to follow the discussion. These scripts are kept for
reproducibility — re-run them after changing data sources, parameters, or
seeds.

```bash
pip install numpy scipy matplotlib pandas statsmodels yfinance powerlaw
python3 scripts/m01.py     # ~10s, needs network for yfinance
python3 scripts/m02.py     # ~10s, needs network
python3 scripts/m03.py     # ~5s, needs network
python3 scripts/m04.py     # ~30s, needs network (100 tickers)
python3 scripts/m05.py     # ~8 minutes (2D Ising Monte Carlo)
python3 scripts/m06.py     # ~5s
python3 scripts/m07.py     # ~15s (Cont-Bouchaud cluster dynamics)
python3 scripts/m08.py     # ~5s (1D reaction-diffusion PDE)
```

The scripts use `matplotlib.use("Agg")` so they run headlessly. If you want
an interactive figure, drop that line and add `plt.show()` at the end.

Seeds are pinned where it matters for reproducibility — varying the seed
will give qualitatively similar but not identical figures.
