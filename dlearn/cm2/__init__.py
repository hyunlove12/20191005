import matplotlib.pyplot as plt
from cm2.face_detect import FaceDetect
from cm2.cat_mosaic import CatMosaic
from cm2.face_mosaic import FaceMosaic

if __name__ == '__main__':
    def print_menu():
        test = ['asdfsadf', 'asdgsad', 'asdf']
        print(test)
        #print(test[:3, 1])

        print('0, EXIT')
        print('1, 얼굴인식')
        print('2, 고양이 모자이크')    #XML파일이 없으면 얼굴 특정 실패
        print('3, 얼굴 모자이크')
        print('4, LENA 이미지 인식')
        print('5, FASHION 이미지 인식')
        print('6, 이미지 편집하기')
        return input('CHOOSE ONE \n')



    while 1:
        menu = print_menu()
        if menu == '0':
            print('EXIT')
            break
        elif menu == '1':
            m = FaceDetect()
            m.read_file()
        elif menu == '2':
            m = CatMosaic()
            m.img_mosaic()
        elif menu == '3':
            m = FaceMosaic()
            m.face_mosaic()
        elif menu == '4':
            pass
        elif menu == '5':
            pass
        elif menu == '6':
            pass
        elif menu == '7':
            pass