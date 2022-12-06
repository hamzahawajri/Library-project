class Book:
    __id_Book = 0

    def __init__(self,title, description, author):
        Book.__id_Book += 1
        self.id = Book.__id_Book
        self.title = title
        self.description = description
        self.author = author
        self.status = ('active', 'inactive')