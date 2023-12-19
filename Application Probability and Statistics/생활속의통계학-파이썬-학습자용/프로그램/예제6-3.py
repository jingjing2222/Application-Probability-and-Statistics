import numpy as np 
import pandas as pd
from scipy import stats

data = pd.read_excel("..\데이터\대학생_수면시간.xlsx")
print(data.describe())

from matplotlib import pyplot as plt
# 수평의 상자도형 (False의 F는 대문자로)
data.boxplot(column=["male", "female"], vert=False)
plt.show()

d1 = pd.read_excel("..\데이터\대학생_수면시간_남자.xlsx")
d2 = pd.read_excel("..\데이터\대학생_수면시간_여자.xlsx")

result=stats.ttest_ind(d1.male, d2.female, equal_var='False')
print(result)

