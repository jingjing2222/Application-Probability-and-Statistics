import pandas as pd
obs_freq = [22, 19, 26, 25, 17, 11]
exp_freq = [20, 20, 20, 20, 20, 20]

from scipy.stats import chisquare
result = chisquare(obs_freq, f_exp=exp_freq)
print(result)
