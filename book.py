from user import User
class Book:
    ISBN_COUNT = 1000 

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.ISBN = Book.ISBN_COUNT
        Book.ISBN_COUNT += 1
        self.is_available = True

    def flatten_book(self) -> dict:
         dict_of_book = {
            
            "title" : self.title,
            "author" : self.author,
            "ISBN" : self.ISBN,
            "is_available" : True,
        }
         return dict_of_book
      

    def __str__(self):
        return f"Title : {self.title}, Author : {self.author}, ISBN : {self.ISBN}, is_availble {self.is_available}"
