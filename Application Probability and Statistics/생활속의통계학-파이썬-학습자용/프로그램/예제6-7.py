#반복이 없는 이원분산분석 
import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# load data file
df = pd.read_excel("..\데이터\이원분석_주행거리.xlsx")

#그룹별 평균 
pivot1 = pd.pivot_table(df, index='car', values='distance')
print(pivot1)
pivot2 = pd.pivot_table(df, index='road', values='distance')
print(pivot2)
print()

model = ols('distance ~ C(road) + C(car)', data=df).fit()
print(anova_lm(model))
print()

# Tukey's test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(endog=df['distance'], groups=df['road'], alpha=0.05)
print(tukey)
print()
tukey = pairwise_tukeyhsd(endog=df['distance'], groups=df['car'], alpha=0.05)
print(tukey)


