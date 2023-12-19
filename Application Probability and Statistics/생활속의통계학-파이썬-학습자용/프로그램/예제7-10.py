import numpy as np
import scipy.stats as st

n=1
p=0.5
x = np.zeros(10)

x = np.random.binomial(n, p, size=10)
print(x)

x=st.binom.rvs(n, p, size=10)
print(x)
