class Author:
    def __init__(self, name):
        self.name = name

    
class Book:
    def __init__(self, title, year, author: Author):
        if not isinstance(author, Author):
            raise TypeError("Error: is not an Author instance")
        self.title = title
        self.year = year
        self.author = author

    def get_info(self):
        return(f"{self.title} by {self.author.name}, {self.year}")

    def change_author(self, new_author: Author):
        if not isinstance(new_author, Author):
            raise TypeError("Error: is not an Author instance")
        self.author = new_author

    def is_classic(self):
        return self.year < 2000


author1 = Author("Robert Martin")
author2 = Author("new Author")
book1 = Book("Clean Code",1995, author1)
print(book1.get_info())
book1.change_author(author2)
print(book1.get_info())
print(book1.is_classic())
