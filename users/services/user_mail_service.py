import os
from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

from users.messages.information_messages  import SUBJECT, LOCAL_MAIL_HOST


class UserMailService:
    SITE_NAME = 'BookStore'
    LOCAL_DOMAIN = '127.0.0.1:8000'
    LOCAL_PROTOCOL = 'http'

    PROD_DOMAIN = 'grisly-spell-88719.herokuapp.com'
    PROD_PROTOCOL = 'https'

    def __init__(self):
        self.mail_template = "users/email/password_reset_email.txt"

    def call(self, user):
        return self.mail_address(user) if self.is_prod() else self.mail_console(user)

    def mail_console(self, associated_user):
        message = self.generate_message(associated_user=associated_user,
                                        domain=UserMailService.LOCAL_DOMAIN,
                                        site_name=UserMailService.SITE_NAME,
                                        protocol=UserMailService.LOCAL_PROTOCOL)

        send_mail(SUBJECT, message, LOCAL_MAIL_HOST , [associated_user.email], fail_silently=False)

    def mail_address(self, associated_user):
        message = self.generate_message(associated_user=associated_user,
                                        domain=UserMailService.PROD_DOMAIN,
                                        site_name=UserMailService.SITE_NAME,
                                        protocol=UserMailService.PROD_PROTOCOL )

        send_mail(SUBJECT, message, settings.EMAIL_HOST_USER, [associated_user.email])

    def generate_message(self, associated_user, domain, site_name, protocol):
        data_for_generate_message = {
            "email":associated_user.email,
            'domain': domain,
            'site_name': site_name,
            "uid": urlsafe_base64_encode(force_bytes(associated_user.pk)),
            "user": associated_user,
            'token': default_token_generator.make_token(associated_user),
            'protocol': protocol,
        }
        return render_to_string(self.mail_template, data_for_generate_message)



    def is_prod(self):
        return 'IS_HEROKU' in os.environ
