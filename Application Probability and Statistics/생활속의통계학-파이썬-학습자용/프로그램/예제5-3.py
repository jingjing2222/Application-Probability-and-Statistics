from scipy.stats import t

df=2
percent_point=0.95 

print('P(t≤k)=0.95, k=',t.ppf(percent_point, df))
