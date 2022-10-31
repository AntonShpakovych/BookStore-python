from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_home_page_get(self):
        client = Client()
        response = client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/pages/home.html')
