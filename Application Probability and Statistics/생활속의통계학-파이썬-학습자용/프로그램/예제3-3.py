from matplotlib import pyplot as plt
# 또는 import matplotlib.pyplot as plt


ratio = [22, 24, 16, 38]                       # 퍼센트 비율
labels = ['pizza', 'hamburger', 'pasta', 'chicken'] 

plt.pie(ratio, labels=labels, autopct='%.1f%%')  #소수이하 첫째자리까지 퍼센트 표시 
plt.show()
