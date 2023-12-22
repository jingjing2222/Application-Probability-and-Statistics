import numpy as np
import pandas as pd

data = pd.DataFrame(pd.read_excel("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/외식비.xlsx"))

print('범위 range')
print(data.max()-data.min())
print('\n')

print('분산 variance')
print(np.var(data))
print('\n')

print('표준편차standard deviation')
print(np.std(data))
print('\n')

print('data 사분위수 편차 quartile deviation')
q25 = data.quantile(0.25)
q75 = data.quantile(0.75)
IRQ = q75 - q25
print(IRQ/2)


"""
print('np 사분위수 편차 quartile deviation')
q25 = np.quantile(data, 0.25, axis=0)
q75 = np.quantile(data, 0.75, axis=0)
IRQ = q75 - q25
print(IRQ/2)
"""

