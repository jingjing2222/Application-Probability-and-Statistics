import numpy as np 
import pandas as pd
from scipy import stats

data = pd.read_excel("..\데이터\피트니스_결과.xlsx")
print(data.describe(), '\n')

from matplotlib import pyplot as plt
# 수평의 상자도형 (False의 F는 대문자로)
data.boxplot(column=["before", "after"], vert=False)
plt.show()

result=stats.ttest_rel(data.before, data.after, alternative='greater')
print(result)
