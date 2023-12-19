import pandas as pd
obs = pd.DataFrame({'남':[26, 20, 11], '여': [10, 15, 18]})
obs.index=['만족', '보통', '불만족']

from scipy.stats import chi2_contingency 
chiresult = chi2_contingency(obs, correction = False)
print(chiresult)
