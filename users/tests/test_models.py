from django.test import TestCase
from users.models import CustomUser
from django.core.exceptions import ValidationError

class TestCustomUserModel(TestCase):
    """CustomUser model, we change required username => email, also we have some custom validation"""

    def setUp(self):
        self.valid_email = 'valid@gmail.com'
        self.invalid_email = 'inva--lidgmail.com'

        self.valid_password = 'Validpassword123'
        self.invalid_password = 'Invalidpassword'

    def test_custom_user_valid_email_password(self):
        user = CustomUser(email=self.valid_email, password=self.valid_password).full_clean()
        self.assertEqual(user, None)

    def test_custom_user_invalid_email_password(self):
        with self.assertRaises(ValidationError):
            CustomUser(email=self.invalid_email, password=self.invalid_password).full_clean()
