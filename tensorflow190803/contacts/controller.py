from contacts.model import ContactsModel
class ContactsController:
    def __init__(self):
        self.model = ContactsModel()

    #staticmethod와 self의 정확한 사용 용도
    @staticmethod
    def print_menu():
        print('1, 연락처 입력 :')
        print('2, 연락처 출력 :')
        print('3, 연락처 삭제 :')
        print('0, 종로 :')
        menu = input('메뉴 선택')
        return menu



    def run(self):
        contacts = []
        while 1:
            menu = self.print_menu()
            if(menu == '1'):
                name = input('이름')
                phone = input('전화번호')
                addr = input('주소')
                email = input('이메일')
                t = self.model.set_contact(name, phone, addr, email)
                contacts.append(t)
            elif(menu == '2'):
                print(self.model.get_contacts(contacts))
            elif(menu == '3'):
                name = input('이름')
                self.model.del_contact(contacts, name)
            elif(menu == '0'):
                print("시스템 종료")
                break
