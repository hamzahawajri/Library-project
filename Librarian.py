class Librarian:
    __id_Librarian = 0

    def __init__(self, full_name, age, id_no):
        Librarian.__id_Librarian += 1
        self.id = Librarian.__id_Librarian
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.employment_type = ('full', 'part')
