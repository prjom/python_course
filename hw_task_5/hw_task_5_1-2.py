import pandas as pd
import numpy as np

print('Задание№1-2')
np.random.seed(0)
data = np.random.randint(1, 11, size=(10, 10))
df = pd.DataFrame(data, index=list('abcdefghij'))

print(df)

# Поиск строки, в которой все числа больше 5
for i, r in df.iterrows():
    if all(r > 5):
        print(f"Строка с индексом {i} содержит только числа больше 5.")
        break
else:
    print("Нет строки, в которой все числа больше 5.")