import pandas as pd
import matplotlib.pyplot as plt


def plot_btc_data(start_date, end_date):
    df = pd.read_csv('BCT-USD.csv')

    df['Date'] = pd.to_datetime(df['Date'])

    # Фильтрация данных по заданному диапазону дат
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    filtered_df.plot(x='Date', y=['Open', 'Close'], figsize=(12, 6))
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.title('Графики цены Bitcoin за указанный период')
    plt.legend(['Открытие', 'Закрытие'])
    plt.show()


# Пример использования
start_date = '2021-01-01'
end_date = '2021-12-31'
plot_btc_data(start_date, end_date)