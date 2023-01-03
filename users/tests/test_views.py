from django.test import TestCase, Client
from django.urls import reverse
from users.tests.factories.custom_user import CustomUserFactory
from django.contrib.auth.models import AnonymousUser
from users.models import CustomUser


class TestUserViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_sign_in_page_get(self):
        response = self.client.get(reverse('sign_in'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/pages/sign_in.html')
    
    def test_sign_up_page_get(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/pages/sign_up.html')

    
    def test_logout_page_get(self):
        user = CustomUserFactory.create()
        self.client.force_login(user)
        response = self.client.get(reverse('logout'))
        self.assertIsInstance(response.wsgi_request.user, AnonymousUser)

    def test_password_reset_page_get(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/pages/password_reset.html')
    
    def test_password_reset_done_page_get(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/pages/password_reset_done.html')
