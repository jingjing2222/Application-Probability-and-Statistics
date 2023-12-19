import pandas as pd
from scipy import stats
data = pd.DataFrame(pd.read_excel("..\데이터\외식비.xlsx"))
# 왜도 skewness
print("왜도 : ", stats.skew(data))

# 첨도 Kurtosis
print("첨도 : ", stats.kurtosis(data))
