import tensorflow as tf
import numpy as np
#그래프로 보여주는 것
import matplotlib.pyplot as plt
from tensorflow import keras

#인식시키는것
#숫자를 알려주고 공부시키는것
if __name__ == '__main__':
    mnist = keras.datasets.mnist
    (train_images, train_labels),(test_images, train_labels) = mnist.load_data()

    mnist_idx = 100

    for row in train_images[mnist_idx]:
        for col in row:
            print('%10f' % col, end='')
        print('\n')
    print('\n')

    plt.figure(figsize=(5,5))
    image = train_images[mnist_idx]
    plt.imshow(image)
    plt.show()