import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла CSV
df = pd.read_csv('emojis.csv')

# Получение количества созданных эмоджи за каждый год
emoji_counts = df['Year'].value_counts().sort_index()

# Построение графика
emoji_counts.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Год')
plt.ylabel('Количество созданных эмоджи')
plt.title('Статистика создания эмоджи по годам')
plt.show()