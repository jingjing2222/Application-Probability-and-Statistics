from scipy.stats import norm

mu=0
sigma=1
percent_point=0.9 

print('P(Z≤k)=0.9, k=',norm.ppf(percent_point, mu, sigma))
