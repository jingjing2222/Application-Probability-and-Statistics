
import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

x = np.arange(5, 100, 5)

np.random.seed(10)
sample_std = np.zeros(len(x))
for i in range(0, len(x)):
      sample_mean = np.zeros(100)
      for j in range(0, 100):
          sample = uniform.rvs(size = x[i])
          sample_mean[j] = np.mean(sample)
      sample_std[i] = np.std(sample_mean, ddof=1)

plt.plot(x, sample_std)
plt.xlabel('number of samples')
plt.ylabel('std of means')
plt.show()
