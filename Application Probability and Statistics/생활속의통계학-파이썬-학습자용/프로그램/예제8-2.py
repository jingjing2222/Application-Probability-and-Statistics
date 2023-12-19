import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

np.random.seed(30)

n = 1000
x = np.zeros(n)
mean = np.zeros(n)

HIST_BINS =  np.linspace(0, 1, 20)
x = np.random.uniform(0, 1, 10000)

fig, ax  = plt.subplots()
fig.subplots_adjust(bottom=0.25)

# 표본수에 따라 표본을 추출하고 평균 값을 mean에 저장(number는 표본수)
def samples(number):
    for i in range(0, 1000):
        sample = np.zeros(number)
        sample = np.random.choice(x, size=number)
        mean[i]=sample.mean()
    return mean

# 초기 도형(앞서 생성한 1000개의 난수에 대해 표본수 2개인 
ax.hist(samples(2), HIST_BINS, edgecolor='black') 

# slider 생성 
num_bin = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='blue')
slider_value = Slider(num_bin, '# of samples', 2, 30, valinit=2, valstep=2)

def update(val):
    ax.axes.clear()
    ax.hist(samples(val), HIST_BINS, edgecolor='black')  
    
slider_value.on_changed(update)
plt.show()


