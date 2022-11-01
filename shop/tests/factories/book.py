import factory
from factory.fuzzy import FuzzyInteger, FuzzyDecimal
from shop.tests.factories.author import AuthorFactory
from shop.tests.factories.category import CategoryFactory
from shop.models import Book



class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words = 2)
    description = factory.Faker('paragraph', nb_sentences = 10)
    quantity = FuzzyInteger(1, 100)
    price = FuzzyDecimal(10, 100.0)
    width = FuzzyDecimal(10, 20.0)
    length = FuzzyDecimal(10, 20.0)
    height = FuzzyDecimal(10, 20.0)
    materials = factory.Faker('sentence', nb_words = 1)
    year_of_publication = FuzzyInteger(2000, 2022)
    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def authors(self, _create, extracted, **kwargs):
        if extracted:
            for author in extracted:
                self.authors.add(author)
        else:
            for _ in range(2):
                self.authors.add(AuthorFactory.create().id)
