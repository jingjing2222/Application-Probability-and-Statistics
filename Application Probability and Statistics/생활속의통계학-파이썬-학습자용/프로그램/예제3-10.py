import pandas as pd
from scipy import stats

data = pd.DataFrame(pd.read_excel("..\데이터\외식비_3개.xlsx"))

print(data.describe())
print()
print(stats.describe(data))


