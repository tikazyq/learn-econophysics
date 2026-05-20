import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

L = 200
dx = 0.1
x = np.arange(L) * dx - L * dx / 2

D = 0.05
nu = 0.5
dt = 0.02
T = 2500
kappa = 0.15      # relaxation rate toward the equilibrium V-shaped supply

soft = np.exp(-(x / 0.5)**2)
rho_B_eq = np.maximum(-x, 0) + 0.3 * soft
rho_A_eq = np.maximum(x, 0) + 0.3 * soft
rho_B = rho_B_eq.copy()
rho_A = rho_A_eq.copy()

J_meta_start, J_meta_end = 400, 1200
J_meta_x = 0.0       # inject at the current price
J_meta_amp = 12.0

prices = []
for t in range(T):
    react = nu * rho_B * rho_A * dt
    rho_B -= react
    rho_A -= react
    rho_B = np.maximum(rho_B, 0)
    rho_A = np.maximum(rho_A, 0)

    rho_B[1:-1] += D * dt / dx**2 * (rho_B[2:] - 2 * rho_B[1:-1] + rho_B[:-2])
    rho_A[1:-1] += D * dt / dx**2 * (rho_A[2:] - 2 * rho_A[1:-1] + rho_A[:-2])

    # Relaxation source: new limit orders refill toward the equilibrium V profile.
    rho_B += kappa * (rho_B_eq - rho_B) * dt
    rho_A += kappa * (rho_A_eq - rho_A) * dt

    if J_meta_start <= t < J_meta_end:
        idx = np.argmin(np.abs(x - J_meta_x))
        rho_B[idx] += J_meta_amp * dt

    p_t = x[np.argmin(np.abs(rho_B - rho_A))]
    prices.append(p_t)

prices = np.array(prices)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
axes[0].plot(x, rho_B, "b-", label=r"$\rho_B$")
axes[0].plot(x, rho_A, "r-", label=r"$\rho_A$")
axes[0].axvline(prices[-1], color="k", ls="--", label="price")
axes[0].set_title("Final density profiles")
axes[0].set_xlabel("price")
axes[0].legend()

axes[1].plot(prices)
axes[1].axvspan(J_meta_start, J_meta_end, color="orange", alpha=0.3, label="meta-order")
axes[1].set_xlabel("time")
axes[1].set_ylabel("price")
axes[1].set_title("Price impact of meta-order")
axes[1].legend()

plt.tight_layout()
plt.savefig("/home/user/learn-econophysics/src/assets/m08-donier-pde.png",
            dpi=110, bbox_inches="tight")

p0 = prices[J_meta_start - 1]
p_peak = prices[J_meta_end - 1]
p_end = prices[-1]
print(f"price before meta-order: {p0:.3f}")
print(f"price at meta-order end (t={J_meta_end}): {p_peak:.3f}  "
      f"(impact = {p_peak - p0:+.3f})")
print(f"price at simulation end (t={T}): {p_end:.3f}  "
      f"(residual = {p_end - p0:+.3f}, "
      f"reversion = {(p_peak - p_end) / (p_peak - p0) * 100:.1f}% of peak impact)")
