from turtle import home
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import home_page, books

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_page)
    
    def test_books_url_is_resolved(self):
        url = reverse('books')
        self.assertEqual(resolve(url).func, books)
