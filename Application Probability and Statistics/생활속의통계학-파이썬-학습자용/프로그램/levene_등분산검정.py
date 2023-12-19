import numpy as np 
import pandas as pd
from scipy import stats

a1 = pd.read_excel("..\데이터\성인_스마트폰_이용시간_남자.xlsx")
a2 = pd.read_excel("..\데이터\성인_스마트폰_이용시간_여자.xlsx")

b1 = pd.read_excel("..\데이터\대학생_수면시간_남자.xlsx")
b2 = pd.read_excel("..\데이터\대학생_수면시간_여자.xlsx")

result1 = stats.levene(a1.male, a2.female, center='mean')
result2 = stats.levene(b1.male, b2.female, center='mean')

print(result1)
print(result2)
