import pandas as pd

df = pd.DataFrame(pd.read_excel("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/missing.xlsx"))
print(df)
print()
print('height=', df.height.mean())
print('weight=', df.weight.mean())
print(df.fillna(df.height.mean()))
print()
print(df)
      