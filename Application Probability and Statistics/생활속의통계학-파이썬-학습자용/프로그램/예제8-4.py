import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

np.random.seed(30)

n = 1000
x = np.zeros(n)
mean = np.zeros(n)

HIST_BINS =  np.linspace(0, 1, 20)
x = np.random.uniform(0, 1, 10000)

fig, ax  = plt.subplots()
fig.subplots_adjust(bottom=0.15)

# 표본수에 따라 표본을 추출하고 평균 값을 mean에 저장(number는 표본수)
def samples(number):
    for i in range(0, 1000):
        sample = np.zeros(number)
        sample = np.random.choice(x, size=number)
        mean[i]=sample.mean()
    return mean

#일시정지 버튼 
pauseax = plt.axes([0.8, 0.025, 0.1, 0.04])
button_pause = Button(pauseax, 'Pause', color='gray')
def pause(event):
    animation.pause()
button_pause.on_clicked(pause)

#다시 재생버튼 
playax = plt.axes([0.6, 0.025, 0.1, 0.04])
button_play = Button(playax, 'Resume', color='gray')
def play(event):
    animation.resume()
button_play.on_clicked(play)

# 프레임에서 불러올 함수 
def update(frame):
    ax.axes.clear()
    ax.set_title('# of samples = '+str(frame))
    ax.hist(samples(frame), HIST_BINS, edgecolor='black')

#애니메이션의 구성 
animation = FuncAnimation(fig, update, frames=np.arange(1, 20, 1), interval=800, repeat=True)
plt.show()

