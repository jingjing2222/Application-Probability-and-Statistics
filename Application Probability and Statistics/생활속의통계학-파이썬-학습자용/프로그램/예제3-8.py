import numpy as np 
import pandas as pd
from scipy import stats

x = pd.read_excel("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/중학생_남자_몸무게.xlsx")

# 평균계산 함수 
print('mean = ', np.mean(x), '\n')

# 중앙값 계산
print('median =', np.median(x),'\n')

# 최빈값 계산
print('mode =', stats.mode(x))
