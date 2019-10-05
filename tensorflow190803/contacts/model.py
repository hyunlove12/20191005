from contacts.contact import Contact
class ContactsModel:
    def __init__(self):
        pass
    #self를 사용하지 않으면 삭제 후 @staticmethod를 붙여준다
    #self -> instance 메소드
    @staticmethod
    def set_contact(name, phone, email, addr):
        contact = Contact(name, phone, email, addr)
        return contact

    @staticmethod
    def get_contacts(params):
        contacts = []
        for i in params:
            contacts.append(i.to_string())
        #들여쓰기 조심
        return ''.join(contacts)

    @staticmethod
    def del_contact(params, name):
        for i, t in enumerate(params):
            if t.name == name:
                del params[i]
