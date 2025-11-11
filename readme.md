⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

UID -> user id counter for users
ISBN_COUNT -> counter for hte books ISBN

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

CLASS:

    User:                                       origin
        self.name : name                   |    from user
        self.id : User.UID                 |    generated in the class counter
        self.borrowed_books : []           |    list of books that the user has 

    Library:                                
        self.library : []                  |   list of books in the library      ->  user input 
        self.users : []                    |   list of the user in the library   -> saved in instance

    Book:
        self.title : title                 |    from user
        self.author : author               |    from user
        self.ISBN : Book.ISBN_COUNT        |    generated in the class counter
        self.is_available : True           |    default

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


                                +------------------+
                                |     DB SCHEMA    |              
                                +------------------+

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
        }  
    ]



⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
