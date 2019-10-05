import matplotlib.pyplot as plt
from digits.hand_writing import HandWriting
if __name__ == '__main__':
    def print_menu():
        test = ['asdfsadf', 'asdgsad', 'asdf']
        print(test)
        #print(test[:3, 1])
        t = [2 == 2]
        print(t)
        print('0, EXIT')
        print('1, 손글씨 인식')
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
            m = HandWriting()
            m.read_file()
        elif menu == '2':
            m = HandWriting()
            m.learning()
        elif menu == '3':
            m = HandWriting()
            fname = './data/my4.png'
            print('테스트')
            print()
            print(m.test(fname))
        elif menu == '4':
            pass
        elif menu == '5':
            pass
        elif menu == '6':
            pass
        elif menu == '7':
            pass