import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import Adam

class Model:
    def __init__(self, input_dim, output_dim, hidden_units=[128, 64], learning_rate=0.001):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_units = hidden_units
        self.learning_rate = learning_rate

    def build(self):
        model = Sequential()
        model.add(Dense(self.hidden_units[0], input_dim=self.input_dim))
        model.add(Activation('relu'))
        model.add(Dropout(0.2))

        for units in self.hidden_units[1:]:
            model.add(Dense(units))
            model.add(Activation('relu'))
            model.add(Dropout(0.2))

        model.add(Dense(self.output_dim))
        model.add(Activation('softmax'))

        optimizer = Adam(lr=self.learning_rate)
        model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

        return model
