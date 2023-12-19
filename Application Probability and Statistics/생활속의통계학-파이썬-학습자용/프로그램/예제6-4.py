from scipy import stats

result=stats.ttest_ind_from_stats(7.02, 1.86, 96, 6.42, 0.96, 99, equal_var='False', alternative='greater')                               
print(result)

