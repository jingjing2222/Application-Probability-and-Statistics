import matplotlib.pyplot as plt
import seaborn as sns

# iris 데이터 불러오기 
iris = sns.load_dataset('iris')
iris.head()

# 산점도 행렬 
sns.pairplot(iris, diag_kind='hist')
plt.show()
