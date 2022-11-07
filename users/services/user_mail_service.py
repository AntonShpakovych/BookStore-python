import os
from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

from users.messages.information_messages  import SUBJECT, LOCAL_MAIL_HOST


class UserMailService:
    def __init__(self):
        self.mail_template = "users/email/password_reset_email.txt"

    def call(self, user):
        return self.mail_address(user) if self.is_prod() else self.mail_console(user)

    def mail_console(self, associated_user):
        c = {
            "email":associated_user.email,
            'domain':'127.0.0.1:8000',
            'site_name': 'BookStore',
            "uid": urlsafe_base64_encode(force_bytes(associated_user.pk)),
            "user": associated_user,
            'token': default_token_generator.make_token(associated_user),
            'protocol': 'http',
            }
        message = render_to_string(self.mail_template, c)
        send_mail(SUBJECT, message, LOCAL_MAIL_HOST , [associated_user.email], fail_silently=False)

    def mail_address(self, associated_user):
        message = render_to_string(self.mail_template)

        send_mail(SUBJECT, message, settings.EMAIL_HOST_USER, [associated_user.email])

    def is_prod(self):
        'IS_HEROKU' in os.environ
