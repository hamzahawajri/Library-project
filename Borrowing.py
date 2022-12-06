from Client import Client
from Book import Book

class Borrowing:

    __id_Borrowing = 0
    __id_Cl = 0
    __id_bo = 0

    def __init__(self,name,date):
        Borrowing.__id_Borrowing += 1
        Borrowing.__id_Cl += 1
        Borrowing.__id_bo += 1
        self.id = Borrowing.__id_Borrowing
        self.name = name
        self.date = date
        self.client_id = Borrowing.__id_Cl
        self.book_id = Borrowing.__id_bo
        self.status = ('active', 'expired', 'canceled')
