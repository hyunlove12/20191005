import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


class FashionModel:
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
        #plt.show()

        train_images = train_images / 255.0
        test_images = test_images / 255.0
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

        #이미지를 맞춰라!
        predictions = model.predict(test_images)
        print(predictions[3])
        #10개 클래스에 대한 예측을 그래프화
        arr = [predictions, test_labels, test_images]
        return arr

    def plot_image(self, i, predictions_array, true_label, img) -> []:
        print('========== plot_image 진입 ==========')
        # \ -> 줄바꿔서 코딩할 경우
        predictions_array, true_label, img = \
            predictions_array[i], true_label[i], img[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap=plt.cm.binary)
        #plt.show()
        predicted_label = np.argmax(predictions_array)
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel('{} {:2.0f}% ({})'.format(
                self.class_names[predicted_label],
                100 * np.max(predictions_array),
                self.class_names[true_label]
        ), color=color)

    @staticmethod
    def plot_value_array(i, predictions_array, true_label):
        predictions_array, true_label = predictions_array[i], true_label[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        thisplot = plt.bar(range(10),
                           predictions_array,
                           color = '#777777'
                           )
        plt.ylim([0, 1])
        predicted_label = np.argmax(predictions_array)
        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')
