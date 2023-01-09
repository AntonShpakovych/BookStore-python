from users.forms import CustomUserChangePasswordForm, CustomUserChangeEmailForm


class UserChangeEmailOrPasswordService:

    def __init__(self, user, type, data):
        self.user = user
        self.type = type
        self.data = data

    def call(self):
        self._generate_form()


    def _generate_form(self):
        self.form = self._valid_type()[self.type]
        self.form.set_user(self.user)
        if self.form.is_valid():
            self.form.save()
        
        

    def _valid_type(self):
        return { 'password': CustomUserChangePasswordForm(self.data), 'email': CustomUserChangeEmailForm(self.data) }
