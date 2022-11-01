# from django.test import TestCase
# from shop.queries.books_query import BooksQuery
# from shop.tests.factories.category import CategoryFactory
# from shop.tests.factories.book import BookFactory

# class TestBooksService(TestCase):
#     def setUp(self):
#         self.category_1 = CategoryFactory.create()
#         self.category_2 = CategoryFactory.create()
#         self.books_1 = [BookFactory.create(category = self.category_1, name = 'AAA') for i in range(3)]
#         self.books_2 = [BookFactory.create(category = self.category_2, name = 'BBB') for i in range(3)]
   
#     def test_call_empty_sorter(self):
#         books_query = BooksQuery(filter = self.category_1.id, sorter = '')

#         for book in books_query.call():
#             self.assertIn(book, self.books_1)
#         self.assertEqual(books_query.call()[0].name, 'AAA')# default sorter => by title
    
#     def test_call_with_sorter(self):
#         books_query = BooksQuery(filter = self.category_1.id, sorter = '-price')


#         for book in books_query.call():
#             self.assertIn(book, self.books_1)
        
#         self.assertGreater(books_query.call()[0].price, books_query.call()[1].price )# sorting py price hight to low
