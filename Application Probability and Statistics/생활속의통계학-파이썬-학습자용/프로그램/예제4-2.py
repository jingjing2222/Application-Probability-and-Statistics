import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import binom

n=5
p=0.5

# 0~(n)까지의 리스트 생성(확률변수)
x = np.arange(n+1)
mean, var = binom.stats(n, p)

# list x의 각 확률변수 r에 대한 확률을 list로 생성하여 prob에 저장 
prob = binom.pmf(x, n, p) 

print('mean=', mean, 'var=', var)
plt.bar(x, prob)
plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('binomial distribution(n=5, p=0.5)')
plt.show()
print(prob)
