import pandas as pd
df = pd.DataFrame(pd.read_excel("..\데이터\초등학교3학년_남자.xlsx"))

# 데이터프레임 컬럼명 변경
df.columns = ['height', 'weight']

print(df.describe(), '\n')
import matplotlib.pyplot as plt
plt.scatter(df.height, df.weight) # 산점도
plt.xlabel("height")                 # x축 레이블 지정
plt.ylabel("weight")                 # y축 레이블 지정
plt.grid()                           # 플롯에 격자 보이기
plt.show()                           # 플롯 보이기

import scipy.stats as stats
# 피어슨 상관계수 검정
corr = stats.pearsonr(df.height, df.weight)
print(corr)


