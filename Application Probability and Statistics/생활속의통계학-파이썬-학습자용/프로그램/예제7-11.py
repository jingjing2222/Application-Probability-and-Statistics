import numpy as np
import scipy.stats as st

loc = 70
scale = 15
x = np.zeros(5)

x = np.random.normal(loc, scale, size=5)
print(x)

x = st.norm.rvs(loc, scale, size=5)
print(x)
