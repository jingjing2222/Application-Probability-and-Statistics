import numpy as np

size=5
x = np.zeros(size)

# 0부터 1사이의 균등분포를 따르는 난수 5개 생성
for i in range(0, size):
     x[i]=np.random.uniform()
     print('x[',i,']=',x[i])
print('\n')

# 1부터 5사이의 균등분포를 따르는 난수 10개 생성
x = np.random.uniform(1, 5, size)
print(x)

