from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.utils import timezone

from .managers import CustomUserManager
from users.validation import ValidationUser


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True, null = False, max_length = ValidationUser.EMAIL_MAXIMUM_LENGTH, validators = [ValidationUser.email_validation])
    password = models.CharField(_('password'),
                                max_length = ValidationUser.PASSWORD_MAX_LENGTH,
                                validators = [ValidationUser.password_validation, MinLengthValidator(ValidationUser.PASSWORD_MIN_LENGTH)],
                                null = False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
