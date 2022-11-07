from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import *

class TestUserUrls(SimpleTestCase):
    """Also we have url from social_django"""

    def test_sign_in_url_is_resolved(self):
        url = reverse('sign_in')
        self.assertEqual(resolve(url).func, sign_in)
    
    def test_sign_up_url_is_resolved(self):
        url = reverse('sign_up')
        self.assertEqual(resolve(url).func, sign_up)
    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, log_out)
