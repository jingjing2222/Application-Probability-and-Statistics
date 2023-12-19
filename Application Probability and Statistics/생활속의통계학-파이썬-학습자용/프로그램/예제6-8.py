import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# load data file
df = pd.read_excel("..\데이터\화장품_매출액.xlsx")
df.columns = ['area', 'service', 'sales']

#그룹별 평균 
pivot1 = pd.pivot_table(df, index='area', values='sales')
print(pivot1)
pivot2 = pd.pivot_table(df, index='service', values='sales')
print(pivot2)
print()

sns.boxplot(x='area', y='sales', hue='service', data=df)
plt.show()

#교호작용 그래프
from statsmodels.graphics.factorplots import interaction_plot
fig = interaction_plot(df.area, df.service, df.sales)
plt.show()
  
model = ols('sales ~ C(area) + C(service) + C(area):C(service)', data=df).fit()
print(anova_lm(model), '\n')

# Tukey's test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=df['sales'], groups=df['area'], alpha=0.05)
print(tukey)
print()
tukey = pairwise_tukeyhsd(endog=df['sales'], groups=df['service'], alpha=0.05)
print(tukey)
