from scipy.stats import norm

mu=0
sigma=1

y1 = norm.cdf(0.5, mu, sigma) 
y2 = norm.cdf(-1.5, mu, sigma) 

print('P(-1.5≤Z≤0.5)=', y1-y2)
