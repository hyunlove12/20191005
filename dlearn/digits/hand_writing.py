import cv2
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split        #지도학습을 위한
from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


class HandWriting:
    def __init__(self):
        self._fname = datasets.load_digits()

    def read_file(self):
        plt.imshow(self._fname.images[0], cmap='gray')
        plt.show()

    def read_nums(self):
        digits = self._fname
        for i in range(15):
            plt.subplot(3, 5, i+1)
            plt.axis('off')
            plt.title(str(digits.target[i]))
            plt.imshow(digits.images[i], cmap='gray')
        plt.show()

    def learning(self):
        digits = datasets.load_digits()
        x = digits.images
        y = digits.target
        x = x.reshape((-1, 64)) #2차원 배열 -> 1차원배열로 변환
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)   #4등분
        clf = svm.LinearSVC()
        clf.fit(x_train, y_train)

        y_pred = clf.predict(x_test)
        print(accuracy_score(y_test, y_pred))
        joblib.dump(clf, './data/digits.pkl')

    @staticmethod
    def test(fname):
        clf = joblib.load('./data/digits.pkl')
        test_img = cv2.imread(fname)
        cv2.imshow('test_img', test_img)
        cv2.waitKey(0)
        test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
        test_img = cv2.resize(test_img, (8, 8))
        test_img = 15 - test_img // 16 # 흑백반전
        test_img = test_img.reshape((-1, 64))
        #글씨(이미지)를 전부 픽셀로 읽어서  1줄로 저장(직렬화)
        # 2차원 배열을 1차원 배열로 변환하기
        res = clf.predict(test_img)
        return res[0]