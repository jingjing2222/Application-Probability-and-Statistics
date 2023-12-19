from scipy.stats import t

df=2
y1 = t.cdf(2, df)
y2 = t.cdf(-2, df)

print('P(-2≤X≤2)=', y1-y2)
