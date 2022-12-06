from Client import Client
from Librarian import Librarian
from Book import Book
from Borrowing import Borrowing
from Library import Library

# add 3 book in library
Bo1 = Book("python", "programming language", "ali")
Bo2 = Book("php-laravel", "programming language", "ahmed")
B03 = Book("c#", "programming language", "hamza")
Lib = Library()
Lib.add_Book(Bo1)
Lib.add_Book(Bo2)
Lib.add_Book(B03)

if __name__ == '__main__':
    while True:
        print("=================================================================")
        print("   Welcome to the library Hamza ,Enter your choice to continue")
        print("=================================================================")
        print("1. Add list of clients ")
        print("2. Add list of librarians ")
        print("3. Add list of books ")
        print("4. Add list of borrowed_orders ")
        print("5. Display_Book_Available")
        print("6. Total_Book_Available")
        print("7. Total_Borrow_book")
        print("8. Exit the library")

        user_choice = input()
        if user_choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("enter valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            full_name = str(input("Enter Fullname :"))

            age = int(input("Enter age :"))

            id_n = int(input("Enter id_n :"))

            phone_number = int(input("phone_number :"))

            cl = Client(full_name, age, id_n, phone_number)

            Lib = Library()

            Lib.add_client(cl)

            for client in Library.Client:  # Client is list []
                print('client ({}, {}, {}, {})'.format(client.id, client.full_name, client.age, client.phone_number))

        if user_choice == 2:
            full_name = str(input("Enter Fullname :"))

            age = int(input("Enter age :"))

            id_n = int(input("Enter id_n :"))

            Li = Librarian(full_name, age, id_n)

            Lib = Library()

            Lib.add_Librarian(Li)

            for librarian in Library.Librarian:  # Librarian is list []
                print('Librarian ({}, {}, {}, {})'.format(librarian.id, librarian.full_name, librarian.age,
                                                          librarian.id_no))

        if user_choice == 3:
            title = str(input("Enter Title :"))

            description = str(input("Enter Description :"))

            author = str(input("Enter Author :"))

            Bo = Book(title, description, author)

            Lib = Library()

            Lib.add_Book(Bo)

            for book in Library.Book:  # Book is list []
                print(
                    'Book ({}, {}, {}, {})'.format(book.id, book.title, book.description, book.author))

        if user_choice == 4:

            for book in Library.Book:  # Book is list []
                print(
                    'Book ({}, {}, {}, {})'.format(book.id, book.title, book.description, book.author))

            req = str(input("What book would you like to borrow? :"))

            da = input("Enter Date : ")

            Bor = Borrowing(req, da)

            Lib = Library()

            Lib.Borrow_book(Bor)

        if user_choice == 5:
            ll = Library()
            ll.DisplayBooksAvailable()

        if user_choice == 6:
            yy = Library()
            yy.TotalBooksAvailable()

        if user_choice == 7:
            ee = Library()
            ee.Total_Borrow_book()


        elif user_choice == 8:
            exit()

        # else:
        #     print("Not a valid option")

        print(" ")
        print("e ----- > exist and c ----- > continue")

        user_choice2 = ""

        while user_choice2 != "c" and user_choice2 != "e":

            user_choice2 = input(': ')

            if user_choice2 == "e":
                exit()

            elif user_choice2 == "c":
                continue
