import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

np.random.seed(1)

n = 100
loc = 70
scale =15
x = np.zeros(n)
# 평균 70, 표준편차 15인 정규분포 난수 100개 생성 
x = np.random.normal(loc, scale, size=n)

fig, ax  = plt.subplots()
fig.subplots_adjust(bottom=0.25)

# 초기 도형(앞서 생성한 100개의 난수에 대해 막대수 5개로 히스토그램 작성)
ax.hist(x, bins = 5, edgecolor='black') 

# slider 생성 
num_bin = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='blue')
slider_value = Slider(num_bin, '# of bins', 5, 15, valinit=5, valstep=1)

def update(val):
    ax.axes.clear()
    ax.hist(x, bins = val, edgecolor='black')  #val 값에 따라 히스토그램 막대수 변경
    
slider_value.on_changed(update)
plt.show()


