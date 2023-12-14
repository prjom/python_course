import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Загрузка данных из файла
data = np.loadtxt('data.txt', delimiter=',')

# Разделение на входные и выходные данные
X = data[:, :-1]
y = data[:, -1]

# Создание модели
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Компиляция модели
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучение модели
model.fit(X, y, epochs=15, batch_size=10, verbose=2)

# Пример предсказания по первым трем строкам датасета
predictions = model.predict(X[:10])
print(predictions)