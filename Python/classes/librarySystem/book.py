class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_available = True

    def is_available(self):
        return self._is_available
    
    def borrow(self):
        if not self._is_available:
            raise RuntimeError("The book is not available")
        self._is_available = False
        
    def return_book(self):
        if self._is_available:
            raise RuntimeError("The book is already available")
        self._is_available = True

