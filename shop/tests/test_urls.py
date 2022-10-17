"""Testing urls"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import home_page

class TestUrls(SimpleTestCase):
    'Testing correct urls'

    def test_home_url_is_resolved(self):
        'home => home_page'

        url = reverse('home')
        self.assertEqual(resolve(url).func, home_page)
