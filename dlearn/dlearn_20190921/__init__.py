from dlearn_20190921.iris import IrisModel
from dlearn_20190921.lena import LenaModel
from dlearn_20190921.fashion import FashionModel
from dlearn_20190921.img_editor import ImgEditor
from dlearn_20190921.Face import Face
import matplotlib.pyplot as plt
if __name__ == '__main__':
    def print_menu():
        print('0, EXIT')
        print('1, IRIS DATA')
        print('2, IRIS SCATTER')
        print('3, 결정경계 그리기')
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
            m = IrisModel()
            print('RESULT :%s' % m.get_iris())
        elif menu == '2':
            m = IrisModel()
            m.draw_scatter()
        elif menu == '3':
            m = IrisModel()
            m.plot_decision_regions()
        elif menu == '4':
            m = LenaModel()
            m.execute()
        elif menu == '5':
            m = FashionModel()
            arr = m.create_model()
            predictions = arr[0]
            test_labels = arr[1]
            img = arr[2]
            i = 20
            plt.figure(figsize=(6, 3))
            plt.subplot(1, 2, 1)
            m.plot_image(i, predictions, test_labels, img)
            plt.subplot(1, 2, 2)
            m.plot_value_array(i, predictions, test_labels)
            plt.show()
            break
        elif menu == '6':
            m = ImgEditor()
            #m.bgr2gray()
            m.img_cut()
        elif menu == '7':
            m = Face()
            # m.bgr2gray()
            m.original()