from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import home_page, books, book


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_page)
    
    # def test_books_url_is_resolved(self):
    #     url = reverse('books')
    #     self.assertEqual(resolve(url).func, books)
    
    # def test_book_url_is_resolved(self):
    #     url = reverse('book', kwargs={'id': 1})
    #     self.assertEqual(resolve(url).func, book)
