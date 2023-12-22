import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
data = pd.read_excel("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/중학생_남자_키.xlsx")

plt.hist(data, label='bins=5', bins=5) #막대수 5
plt.legend()                       #막대수에 대한 범례추가 
plt.show()

plt.hist(data, label='bins=7', bins=7) #막대수 7
plt.legend()
plt.show()

plt.hist(data, label='bins=10', bins=10) #막대수 10
plt.legend()
plt.show()
