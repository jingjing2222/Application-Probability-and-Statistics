import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 100)
plot = sm.qqplot(data, line='45')
plt.show()
