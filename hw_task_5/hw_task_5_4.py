import pandas as pd

# Загрузка данных
df = pd.read_csv('emojis.csv')

# Сортировка DataFrame по столбцу Rank в порядке убывания
df_sorted = df.sort_values(by='Rank', ascending=False)

# Вывод самой популярной подкатегории
popular_subcategory = df_sorted['Subcategory'].iloc[0]
print("Самая популярная подкатегория эмоджи:", popular_subcategory)