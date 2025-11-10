class Book:
  ISBN_COUNT = 1000 

  def __init__(self, title, author):
        self.title = title
        self.author = author
        self.ISBN = Book.ISBN_COUNT
        Book.ISBN_COUNT += 1
        self.is_available = True

class Library:
    def __init__(self):
        self.library = []

    def add_book(self,title,author):
        self.library.append(Book(title,author))

    def print_books(self):
        for book in self.library:
            print(book.title)

library = Library()
library.add_book("brachot","rav ashi")
library.add_book("Shabat","rav ashi")
library.add_book("gitin","rav ashi")

library.print_books()