from shop.queries.books_query import BooksQuery
from shop.models import Category, Book
from shop.services.books_pagination_service import BooksPaginationService

class BooksService:
    def __init__(self, params):
        self.books_query = BooksQuery(filter = params.GET.get('filter'), sorter = params.GET.get('sorter'))
        self.pagination_service = BooksPaginationService(self.books_query.call(), params.GET.get('page')).call()

    def call(self):
        return self._current_filter(), self._current_sorter(), self._sorters(), self._filters(), self.pagination_service

    def _current_filter(self):
        return self.books_query.filter
    
    def _current_sorter(self):
        return self.books_query.sorter

    def _sorters(self):
        return BooksQuery.ORDERS_TYPE

    def _filters(self):
        return { category: Book.objects.filter(category = category).count() for category in Category.objects.all() }
