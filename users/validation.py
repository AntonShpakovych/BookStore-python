from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.messages import validation_messages
import re


class ValidationUser:
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 100
    PASSWORD_MESSAGE = validation_messages.PASSWORD

    EMAIL_MAXIMUM_LENGTH = 63
    EMAIL_MESSAGE = validation_messages.EMAIL

    def password_validation(password, sign_up = True, target='new_password2'):
        PASSWORD_REGEX_TEMPLATE = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])\S+$'
        
        if not re.fullmatch(PASSWORD_REGEX_TEMPLATE, password):
            if sign_up:
                raise ValidationError(
                    _('%(message)s'),
                    params={'message': ValidationUser.PASSWORD_MESSAGE},
                )
            else:
                raise ValidationError({'new_password2': ValidationUser.PASSWORD_MESSAGE})
    
    def email_validation(email):
        EMAIL_REGEX_TEMPLATE = r'([\w+].?)+@[a-z\d\-]+(\.[a-z]+)*\.[a-z]+'

        if not re.fullmatch(EMAIL_REGEX_TEMPLATE, email):
            raise ValidationError(
                _('%(value)s %(message)s'),
                params={'value': email, 'message': ValidationUser.EMAIL_MESSAGE},
            )
class ValidationUserAddress:
    FIRST_NAME_MIN_LENGTH = 3
    FIRST_NAME_MAX_LENGTH = 50
    FIRST_NAME_MESSAGE = validation_messages.ADDRESS_FIRST_NAME

    LAST_NAME_MIN_LENGTH = 3
    LAST_NAME_MAX_LENGTH = 50
    LAST_NAME_MESSAGE = validation_messages.ADDRESS_LAST_NAME

    ADDRESS_MIN_LENGTH = 3
    ADDRESS_MAX_LENGTH = 50
    ADDRESS_MESSAGE = validation_messages.ADDRESS_ADDRESS

    CITY_MIN_LENGTH = 3
    CITY_MAX_LENGTH = 50
    CITY_MESSAGE = validation_messages.ADDRESS_CITY

    ZIP_MIN_LENGTH = 5
    ZIP_MAX_LENGTH = 10
    ZIP_MESSAGE = validation_messages.ADDRESS_ZIP

    PHONE_MAX_LENGTH = 15

    def first_name_validation(first_name):
        FIRST_NAME_REGEX_TEMPLATE = r"[a-zA-z']+"

        if not re.fullmatch(FIRST_NAME_REGEX_TEMPLATE, first_name):
            raise ValidationError(
                _('%(value)s %(message)s'),
                params={'value': first_name, 'message': ValidationUserAddress.FIRST_NAME_MESSAGE},
            )
    
    def last_name_validation(last_name):
        LAST_NAME_REGEX_TEMPLATE = r"[a-zA-z']+"

        if not re.fullmatch(LAST_NAME_REGEX_TEMPLATE, last_name):
            raise ValidationError(
                _('%(value)s %(message)s'),
                params={'value': last_name, 'message': ValidationUserAddress.LAST_NAME_MESSAGE},
            )

    def address_validation(address):
        ADDRESS_REGEX_TEMPLATE = r"[a-zA-Z0-9',\-\s\/]+"

        if not re.fullmatch(ADDRESS_REGEX_TEMPLATE, address):
            raise ValidationError(
                _('%(value)s %(message)s'),
                params={'value': address, 'message': ValidationUserAddress.ADDRESS_MESSAGE},
            )

    def city_validation(city):
        CITY_REGEX_TEMPLATE = r"[a-zA-z']+"

        if not re.fullmatch(CITY_REGEX_TEMPLATE, city):
            raise ValidationError(
                _('%(value)s %(message)s'),
                params={'value': city, 'message': ValidationUserAddress.CITY_MESSAGE},
            )

    def zip_validation(zip):
        ZIP_REGEX_TEMPLATE = r"[0-9-]+"

        if not re.fullmatch(ZIP_REGEX_TEMPLATE, zip):
            raise ValidationError(
                _('%(value)s %(message)s'),
                params={'value': zip, 'message': ValidationUserAddress.ZIP_MESSAGE},
            )
