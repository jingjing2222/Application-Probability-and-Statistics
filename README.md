응용확률및통계  
#
1,2일차
#
리스트

Lst=[1,2] 선언  
Lst.append(value) 끝에 추가  
Lst.insert(index,value) index자리에 value 추가  
Lst.remove(value) value 값 있으면 삭제  
Lst.extend(Lst1) Lst 리스트에 Lst1 리스트 붙이기  
Lst.sort() Lst 정렬  
Lst.reverse() Lst 뒤집기  
#
배열(import numpy as np)  
  
arr1=np.array([1,2,3,4,5])  
arr2=np.array([6,7,8,9,10])  
print(arr1)  
print(arr1-arr2)  + - 말고도 다른 곱셈 나눗셈 가능 단, 배열의 인덱스 수는 같아야함  
np.add(arr1,arr2)  덧셈  
np.subtract(arr1,arr2) 뺄셈  
np.multiply(arr1,arr2) 곱셈  
np.divide(arr1,arr2) 나눗셈  
np.dot(array1,array2) 행렬곱(내적곱)  
  
arr1.sum() 합  
arr1.mean() 평균  
arr1.std() 표준편차  
arr1.var() 분산  
arr1.min() 최소값  
arr1.max() 최대값  
arr1.cumsum() 누적합  
arr1.cumpord() 누적곱  
  
리스트를 배열화 하기도 가능  
  
list1=[[1,2],[3,4]]  
list2=[[5,6],[7,8]]  
  
a=np.array(list1)  
b=np.array(list2)  
  
a=np.zeros(index, dtype=type) index가 index인 type형 0이 들어간 배열 생성 다차원도 가능  
a=np.ones(index, dype=type) index가 index인 type형 1이 들어간 배열 생성 다차원도 가능  
a=np.full(index,value) index가 index인 value값으로 꽉 찬 배열 생성 다차원도 가능  
a=np.empty(index) index가 index인 랜덤 값의 배열 생성 다차원도 가능  
a=np.eye(index) index*index 크기의 2차원 단위 행렬을 생성 단위 행렬은 주대각선상의 요소가 1이고, 나머지 요소가 0인 정사각 행렬  
a=np.array(index) index크기의 0~index-1 value가 들어간 배열 생성  
a=np.arange(-1,1,0.5) 시작점은 -1, 끝점은 1, 간격은 0.5 이러면 총 4칸의 배열 생성  
a=np.linspace(0,1,5) 시작점은 0, 끝점은 1, index가 총 5개인 배열 생성, 이러면 [0,0.25,...,1]  
#
DataFrame(import pandas as pd)

df1=pd.DataFrame([[1,2],[3,4],[5,6]],colums=['a','b'])  
df2=pd.DataFrame({"c":[7,8,9],"d":[10,11,12]})  얘네는 서로 같은 사용법, 다른 문법  

df3=pd.melt(df1) 원래의 열 이름이 'variable' 열에, 해당 값이 'value' 열에 나타남  
df4=pd.concat([df1,df1], axis=0) axis=0은 세로로 합침 이 경우는 3행 2열, 3행 2열인데 열이 서로 같으니 6행 2열의 행렬이 될 것  
df4=pd.concat([df1,df1], axis=1) axis=1은 가로로 합침 이 경우는 3행 2열, 3행 2열인데 그냥 옆으로 붙을 것, 3행 4열의 행렬이 됨  
df5=pd.concat([df1,df2], axis=0) axis=0은 세로로 합치는데, 이 경우 열이 서로 다르므로, NaN값이 추가돼서 6행 4열의 행렬이 됨  
df5=pd.concat([df1,df2], axis=1) axis=1은 가로로 합치는데, 이 경우 옆으로 그냥 붙어서 3행 4열의 행렬이 됨  
df_x = pd.DataFrame([['A', 1], ['B', 2],['C', 3]],columns=['x1', 'x2'])  
df_y = pd.DataFrame({"x1" : ['B', 'C', 'D'],"x3" : [2, 3, 4]})  
df_merge_left=pd.merge(df_x,df_y,how="left") 왼쪽 행렬을 기준으로 병합함, x1이라는 공통 열을 기준에서, df_y의 x1열에 A가 없기 때문에, x3에 NaN을 추가하고, D행은 없어짐  
df_merge_left=pd.merge(df_x,df_y,how="right") 마찬가지로 오른쪽 행렬을 기준으로 병합, df_x 행렬에서 x1열에 D가 없기 때문에, x2에 NaN값을 추가해서 출력, A행은 없어짐  
df_merge_left=pd.merge(df_x,df_y) join의 성격을 갖고 있기에, x1에서 둘 다 가지고 있는 행만 병합함, 이 경우 D가 있는 행, C가 있는 행만 병합함  

df = pd.DataFrame([  
   ['20225001','A', 77],  
   ['20225001','B', 80],  
   ['20225002','A', 85],  
   ['20225002','B', 82],  
   ['20225003','A', 95],  
   ['20225003','B', 90]],  
    columns=['ID_num','Subject', 'Score'])  
df_pivot = df.pivot(index = 'ID_num', columns='Subject', values = 'Score') ID_num을 인덱스로, Subject를 열로, Score를 Values로 행렬을 재배치함  
df_pivot = df.pivot(index='ID_num', columns='Subject', values='Score').sum(axis=1) 다 합함  
group_mean = df.groupby('Subject')['Score'].mean() Subject의 각 Score를 연산해 평균을 냄  
print(df.sort_values(by='Score', ascending=False)) Score기준 내림차순 정렬  
print(df.sort_values(by=['Score', 'Subject'])) Score기준 오름차순 정렬, 같은 값이 있다면 Subject별로 오름차순 정렬 B가 더 크다..!  
print(df.sort_values(by=['Subject', 'Score'])) Subject기준 오름차순 정렬, 같은 값이 있다면 Score별로 오름차순 정렬 B가 더 크다..! 먼저 정렬된다!  
  
file_data = pd.read_csv("경로/파일이름.csv") csv파일을 읽는다 그게 끝이다  
total_score=file_data['점수']*5+file_data['출석'] 점수 열의 데이터 * 5 + 출석 열의 데이터를 DataFrame의 한 열로 만든다. 이는 인덱스를 가진 1차원 배열과 유사하다  
new_data=[file_data['이름'],total_score] 이름 열의 데이터와, total_score의 데이터를 리스트화 한다  
result=pd.concat(new_data,axis=1,keys=['name','total'])  new_data의 리스트를, name, total이라는 열을 생성해 result라는 배열을 생성한다  
result.to_csv("경로/파일이름.csv") csv 파일 생성  
result.to_excel("경로/파일이름.xlsx") excel 파일 생성  
  
df=pd.DataFrame(pd.read_excel("파일경로/파일이름.excel")) 엑셀을 읽는다  
df.info() non-null이 몇개인지, Dtype이 뭔지 알려준다  
df.isnull() NaN인지, 아닌지 체크한다 Nan=True, or False  
df.isnull().sum() NaN의 갯수 체크한다  
df.notnull() NaN인지, 아닌지 체크한다 Nan=False, or False  
df.열이름.mean() 해당 열의 평균을 계산한다  
df=df.fillna(df.열이름.mean()) 결측치인 NaN값에 평균값을 넣는다  
df=df.replace(0,np.nan) 0값에 NaN을 넣는다. 0도 결측치로 따지라는 뜻
df=df.dropna(axis=0) Nan이 존재하는 열을 삭제한다. axis=1이면 행이 사라진다  
#
3일차  
#
import matplotlib.pyplot as plt  
data=pd.read_excel("경로/파일이름.xlsx")  
plt.hist(data, label='bins=5', bins=5) 막대수 5의 막대그래프 출력  
plt.legend() 범례 출력  
plt.show() 출력  
plt.bar(x,y) x, y는 각각 리스트로 x축 y축 막대 그래프를 띄움  
plt.title('제목') 제목 표시  
ratio=[value1, value2,...,valueN]  
labels=['이름1','이름2',...,'이름N']  
plt.pie(ratio, labels=labels, autopct='%.1f%%')  소수 이하 첫째자리까지 퍼센트 표시
plt.show()  
plt.plot(x,y,linestyle={'solid','dashed'}, label='이름') solid=직선, dashed=점선  
plt.legend(loc='best', ncol=n) 범례위치, 행1에 n개의 범례 표시  
plt.boxplot(data, vert={True, False}) True=세로, False=가로
plt.scatter(data.height, data.weight) 산점도 그래프  
plt.xlabel('height') 가로축 이름  
plt.ylabel('weight') 세로축 이름  

import seaborn as sns  
iris = sns.load_dataset('iris')  
iris.head  데이터 불러오기
sns.pairplot(iris, diag_kind='hist)  산점도 행렬 출력
plt.show()  

from scipy import stats  
print(stats.mode(x)) 최빈값 출력  

q25=data.quantile(0.25)  
q75=data.quantile(0.75)  
IRQ=q75-q25  
#
print(IRQ/2) 데이터 사분위수 편차 quartile deviation  

print(data.describe()) pandas에서 제공하는 함수, 개수, 평균, 표준편차, 최소, 최대, 25%, 50%, 75%값 제공  
print(stats.describe(data)) stats에서 제공하는 함수 데이터 개수, 최대 최소, 평균, 분산, 왜도, 첨도 출력  
