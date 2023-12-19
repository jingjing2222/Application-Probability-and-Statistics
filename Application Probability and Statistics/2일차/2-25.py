import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_excel("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/missing.xlsx"))
print(df)
df=df.replace(0,np.nan)
print()
print(df)