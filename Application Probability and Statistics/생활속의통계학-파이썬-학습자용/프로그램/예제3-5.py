import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/스마트폰_이용시간.csv")

print('median = ', np.median(data))
print('min = ', np.min(data),'\n')

plt.boxplot(data, vert=True)           # 수평의 상자도형 (False의 F는 대문자로)
plt.show()    
