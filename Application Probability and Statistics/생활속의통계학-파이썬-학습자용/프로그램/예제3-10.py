import pandas as pd
from scipy import stats

data = pd.DataFrame(pd.read_excel("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/외식비_3개.xlsx"))

print(data.describe())
print()
print(stats.describe(data))