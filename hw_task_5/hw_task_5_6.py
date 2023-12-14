import pandas as pd


def emoji_category_percent(category):
    df = pd.read_csv('emojis.csv')

    # Проверка наличия категории
    category_count = df[df['Category'] == category].shape[0]
    if category_count == 0:
        return f"Категория '{category}' отсутствует в наборе данных."

    # Вычисление процента эмоджи по категории
    total_count = df.shape[0]
    percentage = (category_count / total_count) * 100

    return f"Процент эмоджи по категории '{category}': {percentage:.2f}%"


# Пример использования
category = "Smileys & Emotion"
result = emoji_category_percent(category)
print(result)
