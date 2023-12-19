# Percent point function (inverse of cdf percentiles)
# t.ppf(q, df, loc=0, scale=1)
from scipy.stats import t
print(t.ppf(0.975, 10-1))
print(t.ppf(0.025, 10-1))
