from django.core.paginator import Paginator


class BooksPaginationService:
    QUANTITY_BOOKS_ON_PAGE = 12

    def __init__(self, books, page_number):
        self.paginator = Paginator(books, self.QUANTITY_BOOKS_ON_PAGE)
        self.page_number = page_number

    def call(self):
        return self.paginator.get_page(self.page_number)
