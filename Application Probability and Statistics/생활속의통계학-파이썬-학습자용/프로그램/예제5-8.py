import numpy as np
import scipy.stats as st
from scipy.stats import t

a = [260, 265, 250, 270, 272, 258, 262, 268, 270, 252]

print('평균=', np.mean(a),'\n')
print('표준오차=', st.sem(a),'\n')

print('t값=', t.ppf(0.975, 10-1),'\n')
print('신뢰구간 t.interval =')
print(st.t.interval(0.95, len(a)-1, loc=np.mean(a), scale=st.sem(a)))


