import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

#enter data for three groups
a = [25, 29, 27, 23, 22, 25]
b = [34, 36, 38, 32, 35, 35]
c = [29, 31, 27, 26, 25, 27]

print('a mean=', np.mean(a), 'a std=', np.std(a))
print('b mean=', np.mean(b), 'b std=', np.std(b))
print('c mean=', np.mean(c), 'c std=', np.std(c),'\n')

plot_data = [a, b, c]
ax = plt.boxplot(plot_data, vert=True, meanline=True)
ax = plt.xticks([1, 2, 3], ['A', 'B', 'C'])
plt.show()
print('\n')

# one-way ANOVA
print(f_oneway(a, b, c), '\n')

# DataFrame 으로 배열로 변환  
df = pd.DataFrame({'product': a+b+c, 'group':np.repeat(['a', 'b', 'c'], repeats=6)})

# Tukey's HSD test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=df['product'], groups=df['group'], alpha=0.05)
print(tukey)
