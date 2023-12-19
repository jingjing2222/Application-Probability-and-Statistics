import pandas as pd
from scipy import stats

x = pd.read_excel(("..\데이터\중학생_남자_몸무게.xlsx"))

# 10% 절사평균 계산
print('trimmed mean = ', stats.trim_mean(x, 0.1))
