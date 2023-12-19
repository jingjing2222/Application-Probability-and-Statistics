import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(pd.read_excel("..\데이터\초등학생_키몸무게.xlsx"))

plt.scatter(data.height, data.weight)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()


