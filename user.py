class User:
    UID = 2000

    def __init__(self, name):
        self.name = name
        self.id = User.UID
        User.UID += 1
        self.borrowed_books = []

    def flatten_user(self) -> dict:
        dict_of_user = {}  
        dict_of_user["name"] = self.name
        dict_of_user["id"] = self.id
        dict_of_user["borrowed_books"] = []
        return dict_of_user
     

    def __str__(self):
        return f"User : {self.name}, uid : {self.id}, borrowed books : {self.borrowed_books}"
