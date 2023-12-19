import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

data = pd.DataFrame(pd.read_excel("..\데이터\커피가격.xlsx"))
mu = 3055

# data에 대한 기술통계량 출력
print(data.describe())

plt.hist(data, label='Coffee Price', bins=7)    # 막대 수를 7개로 하고 범례 내용 작성
plt.legend()                                                 # 범례('bins=5')를 그래프에 배치함
plt.show()                                                    # 히스토그램을 화면에 출력

# 만약 양측검정이라면
result = stats.ttest_1samp(data.coeffee, mu, alternative='two-sided')
print(result)

# [예제 1]과 같은 단측검정의 경우
result = stats.ttest_1samp(data.coeffee, mu, alternative='greater')
print(result)
