import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import t

df=2
x = np.arange(-4, 4, 0.01)
y = t.pdf(x, df)

plt.bar(x, y)
plt.xlabel('X')
plt.ylabel('f(X)')
plt.title('t distribution(df=2)')
plt.show()
