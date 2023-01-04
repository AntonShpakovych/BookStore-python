from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django_countries.fields import CountryField

from .managers import CustomUserManager
from users.validation import ValidationUser, ValidationUserAddress


class Address(models.Model):
    first_name = models.CharField(max_length=ValidationUserAddress.FIRST_NAME_MAX_LENGTH,
                                  validators=[ValidationUserAddress.first_name_validation, MinLengthValidator(ValidationUserAddress.FIRST_NAME_MIN_LENGTH)])
    last_name = models.CharField(max_length=ValidationUserAddress.LAST_NAME_MAX_LENGTH,
                                 validators=[ValidationUserAddress.last_name_validation, MinLengthValidator(ValidationUserAddress.LAST_NAME_MIN_LENGTH)])
    phone = models.CharField(max_length=ValidationUserAddress.PHONE_MAX_LENGTH) # other validation implemented in form
    city = models.CharField(max_length=ValidationUserAddress.CITY_MAX_LENGTH,
                            validators=[ValidationUserAddress.city_validation, MinLengthValidator(ValidationUserAddress.CITY_MIN_LENGTH)])
    country = CountryField()
    zip = models.CharField(max_length=ValidationUserAddress.ZIP_MAX_LENGTH,
                          validators=[ValidationUserAddress.zip_validation, MinLengthValidator(ValidationUserAddress.ZIP_MIN_LENGTH)])
    address = models.CharField(max_length=ValidationUserAddress.ADDRESS_MAX_LENGTH,
                               validators=[ValidationUserAddress.address_validation, MinLengthValidator(ValidationUserAddress.ADDRESS_MIN_LENGTH)])

    class Meta:
        abstract=True

    


class ShippingAddress(Address):
    pass

class BillingAddress(Address):
    pass

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True, null = False, max_length = ValidationUser.EMAIL_MAXIMUM_LENGTH, validators = [ValidationUser.email_validation])
    password = models.CharField(_('password'),
                                max_length = ValidationUser.PASSWORD_MAX_LENGTH,
                                validators = [ValidationUser.password_validation, MinLengthValidator(ValidationUser.PASSWORD_MIN_LENGTH)],
                                null = False)
    billing_address = models.OneToOneField(BillingAddress, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')
    shipping_address = models.OneToOneField(ShippingAddress, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
