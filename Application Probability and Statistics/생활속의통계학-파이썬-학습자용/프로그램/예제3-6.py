import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(pd.read_excel("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/초등학생_키몸무게.xlsx"))

plt.scatter(data.height, data.weight)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()


