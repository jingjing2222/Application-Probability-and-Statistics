import pandas as pd

# 고객 데이터프레임 생성
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})

# 주문 데이터프레임 생성
df_orders = pd.DataFrame({
    'OrderID': [100, 101, 102, 103],
    'CustomerID': [2, 2, 4, 3],
    'OrderAmount': [250, 150, 100, 200]
})

# 고객 ID를 기준으로 데이터프레임 병합
merged_df = pd.merge(df_customers, df_orders, on='CustomerID')
sort_df=(merged_df.sort_values(by=['CustomerID','OrderID']))
print(sort_df)
