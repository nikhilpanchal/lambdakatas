import numpy as np
import scipy.stats as stats

d1 = lambda S0, K, r, sigma, T: (np.log(S0/K) + (r + sigma**2/2)*T) / (sigma * np.sqrt(T))

d2 = lambda S0, K, r, sigma, T: (np.log(S0 / K) + (r - sigma**2 / 2) * T) / (sigma * np.sqrt(T))

black_scholes = lambda type, S0, K, r, sigma, T: \
    S0 * stats.norm.cdf(d1(S0, K, r, sigma, T)) - K * np.exp(-r * T) * stats.norm.cdf(d2(S0, K, r, sigma, T)) \
    if type == "C" else \
    K * np.exp(-r * T) * stats.norm.cdf(-d2(S0, K, r, sigma, T)) - S0 * stats.norm.cdf(-d1(S0, K, r, sigma, T))


if __name__ == "__main__":
    print(black_scholes("C", 100, 120, 0.1, 0.35, 10))