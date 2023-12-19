import numpy as np
import scipy.stats as st

size=5
x = np.zeros(size)
x = st.uniform.rvs(3, 10, size)
print(x)

