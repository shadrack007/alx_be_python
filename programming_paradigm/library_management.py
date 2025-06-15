class Boom:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    

class Library:
    _books = []

    def add_book(self, book):
        self._books.append(book)
        

    def check_out_book(self, title):
        pass

    def return_book(self, title):
        try:
            for i in range(0, len(self._books)):
                book = self._books[i]

                if book.title == title:
                    self._books.remove(book)
                    return
                raise ValueError
        except ValueError:
            print('The book is not available')
        

    def list_available_books(self):
        for i in range(0, len(self._books)):
            print(f'{self._books[i].title} by {self._books[i].author} ')