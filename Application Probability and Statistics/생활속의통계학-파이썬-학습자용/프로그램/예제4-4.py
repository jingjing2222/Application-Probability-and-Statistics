from scipy.stats import binom

n=100
p=0.5
percent_point=0.95 

print('P(X≤k)=0.95, k=',binom.ppf(percent_point, n, p))
