﻿import pandas as pd
# <예제 2-13>의 df 사용
df = pd.DataFrame([
   ['20225001','A', 77],
   ['20225001','B', 80],
   ['20225002','A', 85],
   ['20225002','B', 82],
   ['20225003','A', 90],
   ['20225003','B', 90]],
    columns=['ID_num','Subject', 'Score'])
print(df, '\n')

print(df.sort_values(by='Score', ascending=False))

print(df.sort_values(by=['Score', 'Subject'],ascending=False))

print(df.sort_values(by=['Subject', 'Score'],ascending=False))





      
