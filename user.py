class User:
    UID = 2000

    def __init__(self, name):
        self.name = name
        self.id = User.UID
        User.UID += 1
        self.borrowed_books = []

 

    def __str__(self):
        return f"User : {self.name}, uid : {self.id}, borrowed books : {self.borrowed_books}"
