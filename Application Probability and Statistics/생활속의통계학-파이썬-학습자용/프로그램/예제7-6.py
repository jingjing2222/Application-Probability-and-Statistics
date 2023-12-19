import numpy as np

size=5
x = np.zeros(size)


np.random.seed(1)
# case 1: 0부터 1사이의 균등분포를 따르는 난수 5개 생성
x=np.random.uniform(0, 1, size)
print('case1: ', x,'\n')

# case 2: 0부터 1사이의 균등분포를 따르는 난수 5개 생성(case 1과 다름)
x=np.random.uniform(0, 1, size)
print('case2: ', x,'\n')

np.random.seed(1)
# case 3: 0부터 1사이의 균등분포를 따르는 난수 5개 생성(case 1과 동일)
x=np.random.uniform(0, 1, size)
print('case3: ', x,'\n')
