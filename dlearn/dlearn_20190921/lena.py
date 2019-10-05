import cv2


class LenaModel:
    def __init__(self):
        self.fname = './data/lena.jpg'

    def execute(self):
        original = cv2.imread(self.fname, cv2.IMREAD_COLOR)
        gray = cv2.imread(self.fname, cv2.IMREAD_GRAYSCALE)
        unchanged = cv2.imread(self.fname, cv2.IMREAD_UNCHANGED)

        """
        이미지 읽기에는 위 3가지 속성이 존재함
        대신에 1, 0, -1을 사용해도 됨
        """

        cv2.imshow('Original', original)
        cv2.imshow('Gray', gray)
        cv2.imshow('Unchanged', unchanged)
        cv2.waitKey(0)
        cv2.destroyAllWindows() #윈도우 종료 // 쓰레드 종료해주어야

