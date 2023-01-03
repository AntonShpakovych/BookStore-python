from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.messages.validation_messages import EMAIL, PASSWORD
import re


class ValidationUser:
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 100
    PASSWORD_MESSAGE = PASSWORD

    EMAIL_MAXIMUM_LENGTH = 63
    EMAIL_MESSAGE = EMAIL

    def password_validation(password):
        PASSWORD_REGEX_TEMPLATE = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])\S+$'
        

        if not re.fullmatch(PASSWORD_REGEX_TEMPLATE, password):
            raise ValidationError(
                _('%(message)s'),
                params={'message': ValidationUser.PASSWORD_MESSAGE},
            )
    
    def email_validation(email):
        EMAIL_REGEX_TEMPLATE = r'([\w+].?)+@[a-z\d\-]+(\.[a-z]+)*\.[a-z]+'

        if not re.fullmatch(EMAIL_REGEX_TEMPLATE, email):
            raise ValidationError(
                _('%(value)s %(message)s'),
                params={'value': email, 'message': ValidationUser.EMAIL_MESSAGE},
            )
