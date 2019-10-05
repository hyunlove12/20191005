import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


class FashionChecker:
    def __init__(self):
        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                            'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def create_model(self) -> []:
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()    #self데이터 전처리 과정
        plt.figure()
        plt.imshow(train_images[10])
        plt.colorbar()
        plt.grid(False)
        plt.show()

        #train_images = train_images / 255.0
        #test_images = test_images / 255.0
        #모델링
        model = keras.Sequential([
                keras.layers.Flatten(input_shape=(28, 28)),        #딥 러닝 -> 멀티 레이어
                keras.layers.Dense(128, activation='relu'),  #활성화 함수
                keras.layers.Dense(10, activation='softmax')
        ])
        #하나로 밀집
        model.compile(
                      optimizer='adam'
                    , loss = 'sparse_categorical_crossentropy'
                    , metrics=['accuracy']
                      )
        #Learning
        model.fit(train_images, train_labels, epochs=5)
        #test
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        print('테스트 정확도 : {}'.format(test_acc))