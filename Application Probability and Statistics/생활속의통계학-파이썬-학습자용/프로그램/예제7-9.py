import numpy as np
from matplotlib import pyplot as plt

n=1000
size=100
x = np.zeros(n)
mean = np.zeros(n)

for i in range(0, n):
    x=np.random.uniform(0, 1, n)
    x=np.random.choice(x, size)
    mean[i]=x.mean()

plt.hist(mean, bins=20) 
plt.show()
