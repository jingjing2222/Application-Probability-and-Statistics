import pandas as pd
obs = pd.DataFrame({'남':[25, 75], '여': [45, 55]})
obs.index=['찬성', '반대']

from scipy.stats import chi2_contingency 
chiresult = chi2_contingency(obs, correction = False)
print(chiresult)
