from book import Book
from user import User

class Library:
    """
    add_book -> 🟩
    add_user ->  🟩
    borrow_book -> 🟩
    return_book -> 
    print_books_title -> 🟩
    print_books ->  🟩
    """
    def __init__(self):
        self.library = []
        self.users = []

    def add_book(self,title,author):
        self.library.append(Book(title,author))

    #TODO: REMOVE TEST 
    def add_user(self):
        # new_user_name = input("enter new user name: ")
        new_user_name = "test name"
        new_user = User(new_user_name)
        self.users.append(new_user)

    def borrow_book(self,user_id,book_to_borrow):
        # pass to is_availble -> title or id -> get book object
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
                

    def print_books_titles(self):
        for book in self.library:
            print(book.title)

    def print_books(self):
        for book in self.library:
            print(book)

    def change_name_by_id(self,new_name,id):
        for user in library.users:
            if user.id == id:
                user.name = new_name

    def flatten_library(self) -> list[dict]:
        """
        library = [
        #library main
        {
            list_of_books : self.library,
            list_of_users : self.users,
            number_of_books : len(self.library),
        },
        #books
        {
            ISBN_COUNT : ISBN_COUNT, #  -> the count of the curent id book 
            title : title,
            author : author,
            ISBN : Book.ISBN_COUNT,
            is_available : True,
        },
        #users
        {
            name : name,
            id : User.UID,
            borrowed_books : [],
        }   `   
    ]  
    """
        library = []

        books = []
        for book in self.library:
            current = book.flatten_book()
            books.append(current)
        



















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
# library.print_books()

library.borrow_book(2000,"brachot")

print()
print()
print("=============")
print()
print("BOOK LIST")
print(library)
library.print_books()

("=============")


