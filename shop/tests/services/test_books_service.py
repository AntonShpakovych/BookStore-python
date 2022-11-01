# from django.test import TestCase
# from django.test.client import RequestFactory

# from shop.tests.factories.category import CategoryFactory
# from shop.tests.factories.book import BookFactory

# from shop.models import Book
# from shop.models import Category

# from shop.services.books_service import BooksService
# from shop.queries.books_query import BooksQuery
# from shop.services.books_pagination_service import BooksPaginationService



# class TestBooksService(TestCase):
#     def setUp(self):
#         self.category_1 = CategoryFactory.create()
#         self.category_2 = CategoryFactory.create()
#         self.books_1 = [BookFactory.create(category = self.category_1) for i in range(3)]
#         self.books_2 = [BookFactory.create(category = self.category_2) for i in range(3)]
#         self.DEFAULT_SORTER = list(BooksQuery.ORDERS_TYPE.keys())[0]
#         self.SORTERS = BooksQuery.ORDERS_TYPE
#         self.FILTERS = { category: Book.objects.filter(category = category).count() for category in Category.objects.all() }

#     def test_call(self):
#         rf = RequestFactory()
#         params = rf.get('/books/', {'filter': self.category_1.id, 'sorter': '', 'page': 1})  # if empty sorter book_query get default_sorter from constant

        

#         book_query = BooksQuery(filter = params.GET.get('filter'), sorter = params.GET.get('sorter'))
#         pagination_service = BooksPaginationService(book_query.call(), params.GET.get('page'))
#         books_service = BooksService(params)
#         expected_result = params.GET.get('filter'), self.DEFAULT_SORTER, self.SORTERS, self.FILTERS, pagination_service.call()
        


#         self.assertEqual(books_service.call()[:-1], expected_result[:-1])
#         self.assertEqual(books_service.call()[-1].object_list[0], expected_result[-1].object_list[0])
