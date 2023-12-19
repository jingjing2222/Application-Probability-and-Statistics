import matplotlib.pyplot as plt
import pandas as pd
file_data = pd.read_csv("Application Probability and Statistics/생활속의통계학-파이썬-학습자용/연습문제 데이터/sample1.csv")
print(file_data[0:5])

total_score=file_data['점수']*5+file_data['출석']
new_data=[file_data['이름'],total_score]

result=pd.concat(new_data,axis=1,keys=['name','total'])

print(result)
result.to_csv("/Users/kimhyeongjeong/Desktop/학부/3-Winter/Application-Probability-and-Statistics/Application Probability and Statistics/2일차/2-17/result1.csv")
result.to_excel("/Users/kimhyeongjeong/Desktop/학부/3-Winter/Application-Probability-and-Statistics/Application Probability and Statistics/2일차/2-17/result1.xlsx")

plt.hist(total_score, label='score data',bins=7)
plt.legend()
plt.savefig("/Users/kimhyeongjeong/Desktop/학부/3-Winter/Application-Probability-and-Statistics/Application Probability and Statistics/2일차/2-17/histogram of score.png")
plt.show()