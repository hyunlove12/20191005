#금융사  크롤리은 불법
#미국은 가능
import numpy as np
import tensorflow as tf
from collections import deque
import random
#케라스(고급) -> 싸이키넌(중급) -> 텐스플로우(입문)

class AITrader:
    def __init__(self):
        pass

    #금융공학 모델
    def model_builder(self):
        model = tf.keras.models.Sequential()
        #층을 쌓는 것
        model.add(tf.keras.layers.Dense(units=32, activation='relu', input_dim=self.state_size))
        model.add(tf.keras.layers.Dense(units=64, activation='relu'))
        model.add(tf.keras.layers.Dense(units=128, activation='relu'))
        model.add(tf.keras.layers.Dense(units=256, activation='relu'))
        model.add(tf.keras.layers.Dense(units=512, activation='relu'))
        model.add(tf.keras.layers.Dense(units=self.action_space, activation='linear'))      #linear 숫자값을 맞추는 것
        model.complie(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=0.01))
        return model

    def trade(self, state):
        if random.random() <= self.epsilon:
            return random.randrange(self.action_space)
        actions = self.model.predict(state)
        return np.argmax(actions[0])

    def batch_train(self, batch_size):
        batch = []
        for i in range(len(self.memory) - batch_size + 1, len(self.memory)):
            batch.append(self.memory[i])





