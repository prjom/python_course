import numpy as np
from keras.models import Sequential
from keras.layers import Dense

class MyModel:
    def __init__(self, num_layers, layer_neurons, activations, loss_function, optimizer):
        self.num_layers = num_layers
        self.layer_neurons = layer_neurons
        self.activations = activations
        self.loss_function = loss_function
        self.optimizer = optimizer
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(self.layer_neurons[0], input_dim=8, activation=self.activations[0]))
        for i in range(1, self.num_layers):
            model.add(Dense(self.layer_neurons[i], activation=self.activations[i]))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss=self.loss_function, optimizer=self.optimizer, metrics=['accuracy'])
        return model

    def prepare_data(self, data_file):
        data = np.genfromtxt(data_file, delimiter=',')
        X = data[:, :-1]
        y = data[:, -1]
        return X, y

    def train(self, X, y, epochs, batch_size):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=2)

    def infer(self, X):
        predictions = self.model.predict(X)
        return predictions

model = MyModel(num_layers=3, layer_neurons=[12, 8, 1], activations=['relu', 'relu', 'sigmoid'], loss_function='binary_crossentropy', optimizer='adam')

X, y = model.prepare_data('data.txt')

model.train(X, y, epochs=15, batch_size=10)

predictions = model.infer(X[:3])
print(predictions)
