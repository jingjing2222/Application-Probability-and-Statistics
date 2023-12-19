import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import RadioButtons

np.random.seed(1)

n = 100
loc = 70
scale =15
x = np.zeros(n)
# 평균 70, 표준편차 15인 정규분포 난수 100개 생성 
x = np.random.normal(loc, scale, size=n)

fig, ax  = plt.subplots()
fig.subplots_adjust(left=0.4)

# 초기 도형(앞서 생성한 100개의 난수에 대해 막대수 5개로 히스토그램 작성)
ax.hist(x, bins = 5, color='yellow', edgecolor='black') 

# RadioButton 생성 
rax = plt.axes([0.1, 0.5, 0.2, 0.2])
radio_button = RadioButtons(rax, ('yellow', 'red', 'blue', 'green'))

def colorfunc(label):
    ax.hist(x, bins = 5, color=label, edgecolor='black')
    plt.draw()
    
radio_button.on_clicked(colorfunc)
plt.show()


