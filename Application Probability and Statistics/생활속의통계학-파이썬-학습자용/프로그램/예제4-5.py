import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

mu=50
scale=5

x = np.arange(mu-30, mu+30, 0.1)
y = norm.pdf(x, mu, scale) 

plt.bar(x, y)
plt.xlabel('X')
plt.ylabel('f(X)')
plt.title('normal distribution(mu=50, sigma=5)')
plt.show()
