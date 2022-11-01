# from django.test import TestCase
# from shop.services.books_pagination_service import BooksPaginationService
# from shop.tests.factories.book import BookFactory


# class TestBooksService(TestCase):
#     """ 12 books per page"""

#     def setUp(self):
#         self.books_per_page = 12
#         self.books = [BookFactory.create() for i in range(24)]

#     def test_call_first_page(self):
#         page_number = 1
#         books_pagination = BooksPaginationService(self.books, page_number)

#         self.assertEqual(books_pagination.call().object_list, self.books[:self.books_per_page])
    
#     def test_call_last_page(self):
#         page_number = 2
#         books_pagination = BooksPaginationService(self.books, page_number)
        
#         self.assertEqual(books_pagination.call().object_list, self.books[self.books_per_page:])
