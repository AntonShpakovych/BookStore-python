from django.test import TestCase
from shop.models import Book
from shop.tests.factories.author import AuthorFactory
from shop.tests.factories.book import BookFactory

class TestModels(TestCase):
    def setUp(self):
        self.authors = [AuthorFactory.create(), AuthorFactory.create()]
        self.book = BookFactory.create(authors = self.authors)

    def test_book_all_authors(self):
        """
            Model Book, has custom method all_authors =>(self.authors)=> 'take all author for current_book and return: first_name last_name, first_name last_name ...'
        """

        result = ', '.join(author.first_name + ' ' + author.last_name for author in self.authors)
        self.assertEqual(self.book.all_authors(), result)
