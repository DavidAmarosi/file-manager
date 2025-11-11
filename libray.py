from book import Book
from user import User

class Library:
   
    def __init__(self):
        self.library = []
        self.users = []

    def add_book(self,title,author):
        self.library.append(Book(title,author))

   
    def add_user(self,user,user_name):
        user = User(user_name)
        self.users.append(user)

    def borrow_book(self,user_id,book_to_borrow):
        check = library.is_availble(book_to_borrow)
        if check:
            for user in library.users:
                if user.id == user_id:
                    user.borrowed_books.append(check)
                    check.is_available = False
        else:
            print("alredy borrowed")

    def return_book(self,user_id, book_isbn):
        for book in self.library:
            if book.ISBN == book_isbn:
                book.is_available = True
                user_id.borrowed_books.remove(book)
    
    def is_availble(self, book_to_borrow):
        if isinstance(book_to_borrow,str):
             for book in self.library:
                  if book_to_borrow == book.title:
                       return book
        else:
            for book in self.library:
                if book.ISBN == book_to_borrow:
                    if book.is_available == True:
                        return book
                else:
                    return False
                

    def print_books(self):
        for book in self.library:
            print(book)

    def change_name_by_id(self,new_name,id):
        for user in library.users:
            if user.id == id:
                user.name = new_name

    def flatten_library(self) -> list[dict]:

        books = []
        for book in self.library:
            current = vars(book)
            books.append(current)

        users = []
        for user in self.users:
            current = vars(user)
            users.append(current)

    def __str__(self):
        title_list = [book for book in self.library]
        return str(title_list)



library = Library()
library.add_book("brachot","rav ashi")
library.add_book("Shabat","rav ashi")
library.add_book("gitin","rav ashi")
library.add_user()
library.add_user()
library.add_user()
library.add_user()
library.borrow_book(2000,"brachot")

print()
print()
print("=============")
print()
print("BOOK LIST")
print(library)
library.print_books()

("=============")


