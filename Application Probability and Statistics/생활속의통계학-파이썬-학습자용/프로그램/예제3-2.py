from matplotlib import pyplot as plt

x = [6, 7, 8, 9, 10, 11]  # x축에 나타낼 6개의 값(리스트 사용)
y = [16109, 41401, 53121, 59899, 53450, 82565] # y축의 값

plt.bar(x, y)                          # x축과 y축의 데이터     
plt.title('number of cases by month')   # 제목 표시 
plt.show()
