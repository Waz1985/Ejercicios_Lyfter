
class Member:
    def __init__(self, name):
        self.name = name
        self._borrowed_books = []

    def borrow_book(self, book):
        if book in self._borrowed_books:
            raise RuntimeError("You already have this book")
        else:
            self._borrowed_books.append(book)
            book.borrow()

    def return_book(self, book):
        if book not in self._borrowed_books:
            raise RuntimeError("This member does not have this book")
        book.return_book()
        self._borrowed_books.remove(book)

    def has_book(self, book) -> bool:
        return book in self._borrowed_books


