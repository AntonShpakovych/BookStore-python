from django.test import TestCase
from users.tests.factories.custom_user import CustomUserFactory
from users.services.user_mail_service import UserMailService
from django.core import mail

class TestUserMailService(TestCase):

    def setUp(self):
        self.user = CustomUserFactory.create()
        self.user_mail_service = UserMailService().call(self.user)

    def test_call(self):
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [self.user.email])
