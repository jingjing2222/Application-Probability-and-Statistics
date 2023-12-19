import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_excel("..\데이터\Galtons Height Data_딸.xlsx"))
df = 2.54 * df

import seaborn as sns
sns.regplot(x=df.father, y=df.daughter)
plt.show()

from statsmodels.formula.api import ols
res = ols('df.daughter ~ df.father', data=df).fit()
print(res.summary())

