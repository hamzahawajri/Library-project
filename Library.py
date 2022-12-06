class Library:
    Client = []
    Book = []
    Librarian = []
    borrowed_orders = []

    def add_client(self, client):
        self.Client.append(client)

    def add_Book(self, book):
        self.Book.append(book)

    def add_Librarian(self, librarian):
        self.Librarian.append(librarian)

    def Borrow_book(self, Borrow):
        # self.borrowed_orders.append(Borrow)
        if Borrow in self.Book:
            self.Book.remove(Borrow)
            print(f"You have borrow a {Borrow} book. Return it within 30 days")
            return True
        else:
            print("Sorry, This book has already been borrow by someone else")
            return False

    def DisplayBooksAvailable(self):
        for book in self.Book:
            print("Book id :", book.id)
            print("book title :", book.title)
            print("Book description :", book.description)
            print("=======================================")

    def TotalBooksAvailable(self):
        print("TotalBooksAvailable is :", len(self.Book))

    def Total_Borrow_book(self):
        print("TotalBooksAvailable is :", len(self.borrowed_orders))

        # if self.Client == client_id and self.Book == book_id:
        #     self.borrowed_orders.pop(Borrow)
        # else:
        #     self.borrowed_orders.remove(Borrow)

    # for client in self.Client:
    #     for book in self.Book:
    #         if client.id == client_id and book.id == book_id:
    #             self.borrowed_orders.append(name)
