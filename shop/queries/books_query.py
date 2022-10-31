from shop.models import Book

class BooksQuery:
    FIRST = 0
    STRING_NONE = 'None'
    ORDERS_TYPE = { 'title': 'Title ASC',
                    '-title': 'Title DESC',
                    '-created': 'Newest first',
                    '-price': 'Price: Hight to low',
                    'price': 'Price: Low to hight' }

    DEFAULT_SORTER = list(ORDERS_TYPE.keys())[FIRST]

    def __init__(self, filter = None, sorter = None, books = Book.objects.all()):
        self.filter = filter
        self.sorter = self._generate_order_by(sorter)
        self.books = books

    def call(self):
        return self._sorting_and_filtering()

    def _books_filter_by_category(self):
        if self.filter and self.filter != self.STRING_NONE:
            return self.books.filter(category = self.filter)

        return self.books

    def _sorting_and_filtering(self):
        return self._books_filter_by_category().order_by(self.sorter)

    def _generate_order_by(self, sorter):
        return sorter if sorter else self.DEFAULT_SORTER
