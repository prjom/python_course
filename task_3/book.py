class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print("Книга находится у абонента")
        else:
            print("Выдаем книгу абоненту")
            self.checked_out = True

    def check_in(self):
        if self.checked_out:
            print("Книга выдана")
            self.checked_out = False
        else:
            print("Принимаем книгу в библиотеку")

my_book = Book("Сказки", 'Народ')

my_book.check_out()
my_book.check_out()

my_book.check_in()
my_book.check_in()