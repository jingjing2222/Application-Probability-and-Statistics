응용확률및통계
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
배열(import numpy ad np)  
  
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
