import pandas as pd
import numpy as np

np.random.seed(0)
data = np.random.randint(1, 11, size=(10, 10))
df = pd.DataFrame(data, index=list('abcdefghij'), columns=list('abcdefghij'))

print("Размерность матрицы:")
print(df.shape)

print("Индексы столбцов:")
print(df.columns)

print("Среднее значение всех чисел матрицы:")
print(df.values.mean())

df.to_csv("matrix.csv", index=False)
print("Матрица успешно записана в CSV.")