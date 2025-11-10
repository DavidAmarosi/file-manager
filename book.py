from user import User
class Book:
    ISBN_COUNT = 1000 

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.ISBN = Book.ISBN_COUNT
        Book.ISBN_COUNT += 1
        self.is_available = True

    def __str__(self):
        return str(["Title : {self.title}, Author : {self.author}, ISBN : {self.ISBN}, is_availble {self.is_available}"])

class Library:
    def __init__(self):
        self.library = []
        self.users = []

    def add_book(self,book):
        self.library.append(book)

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self,user_id, book_isbn):
        

        pass
    def return_book(user_id, book_isbn):
        pass
    def list_available_books():
        pass

    def print_books(self):
        for book in self.library:
            print(book.title)

    def print_books(self):
        for book in self.library:
            print(book)

    def __str__(self):
        title_list = [book for book in self.library]
        return str(title_list)



library = Library()
library.add_book("brachot","rav ashi")
library.add_book("Shabat","rav ashi")
library.add_book("gitin","rav ashi")

# library.print_books()

print(library)
library.print_books()