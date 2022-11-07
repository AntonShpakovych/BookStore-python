from django.test import TestCase, Client
from django.urls import reverse
from shop.tests.factories.book import BookFactory


class TestViews(TestCase):
    def setUp(self):
       self.client = Client()

    def test_home_page_get(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
    
    def test_books_page_get(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/pages/books.html')
    
    def test_book_page_get(self):
        book = BookFactory.create()
        response = self.client.get(reverse('book', kwargs={'id': book.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/pages/book.html')
