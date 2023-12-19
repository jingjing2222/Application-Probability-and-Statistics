from matplotlib import pyplot as plt

x = [2014, 2015, 2016, 2017, 2018, 2019, 2020]  # x축 지점의 값들
y1 = [14.4, 14.5, 15.4, 16.9, 17.8, 17.6, 27.6]	# y1축 지점의 값들
y2 =[20.5, 21.0, 22.8, 23.6, 24.2, 24.3, 29.5]     # y2축 지점의 값들
plt.plot(x, y1, linestyle='solid', label='teens')    # x와 y1 그래프 작성, 선스타일=직선
plt.plot(x, y2, linestyle='dashed',label='20s')    # x와 y2 그래프 작성, 선스타일=점선
                                               # plt.legend(loc='best')   ncol = 1
plt.legend(loc='best', ncol=2)            # 범례위치, 행 1에 두 개(ncol)의 범례표시 
plt.title('Internet Usage Time per Week')   
plt.show()	              
