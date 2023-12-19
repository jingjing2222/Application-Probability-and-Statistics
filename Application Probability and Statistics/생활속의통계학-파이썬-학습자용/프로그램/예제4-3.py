from scipy.stats import binom

n=5
p=0.5

print('P(X≤3)=',binom.cdf(3, n, p))
