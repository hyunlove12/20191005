import cv2

class Face:
    def __init__(self):
        self._fname = './data/test.jpg'

    def orginal(self):
        img = cv2.imread(self._fname)
        #imgshow 파라미터는 무조건 2개(이름과 이미지)
        cv2.imshow('original', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows() #윈도우 종료 // 쓰레드 종료해주어야\