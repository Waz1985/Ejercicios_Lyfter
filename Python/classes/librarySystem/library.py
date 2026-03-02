from book import Book
from member import Member


class Library:
    def __init__(self, name):
        self.name = name
        self._books = []
        self._members = []
    
    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("book is not an instance of Book")
        for b in self._books:
            if b.title == book.title and b.author == book.author:
                raise RuntimeError("This book already exists")
        self._books.append(book)


    def add_member(self, member: Member):
        if not isinstance(member, Member):
            raise TypeError("member is not an instance of Member")
        for m in self._members:
            if m.name == member.name:
                raise RuntimeError("This member already exists")
        self._members.append(member)  

    def has_book(self, book) -> bool:
        return book in self._books

    def has_member(self, member) -> bool:
        return member in self._members

    def lend_book(self, book, member):
        if not self.has_book(book):
            raise RuntimeError("Book not found in Library")
        if not self.has_member(member):
            raise RuntimeError("Member not found in Library")
        if not book.is_available():
            raise RuntimeError("Book is not available")
        member.borrow_book(book)

    def receive_book(self, book, member):
        if not self.has_book(book):
            raise RuntimeError("Book not found in Library")
        if not self.has_member(member):
            raise RuntimeError("Member not found in Library")
        if not member.has_book(book):
            raise RuntimeError("There is no book to return")
        member.return_book(book)
    
    def available_books(self):
        list_available_books = []
        for b in self._books:
            list_available_books.append(b)
        return list_available_books




library = Library("Central")

book = Book("Clean Code", "Robert Martin")
member = Member("Ana")

library.add_book(book)
library.add_member(member)

library.lend_book(book, member)
print(book.is_available())   # False

library.receive_book(book, member)
print(book.is_available())   # True

for book in library.available_books():
    print(book.title, book.author)