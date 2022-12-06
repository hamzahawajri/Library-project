class Client:
    __id_client = 0

    def __init__(self,full_name, age, id_no, phone_number):
        Client.__id_client += 1
        self.id = Client.__id_client
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number

