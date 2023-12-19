import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

np.random.seed(10)
mean_array = np.zeros(1000)
var_array = np.zeros(1000)
for i in range(0, 1000):
      sample = uniform.rvs(size = 100)
      mean_array[i] = np.mean(sample)

import seaborn as sns
sns.histplot(mean_array, bins=20, kde=True)
plt.show()
