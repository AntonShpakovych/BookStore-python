from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from users.models import CustomUser
from users.messages.validation_messages import PASSWORD_MISSMATCH
from users.validation import ValidationUser



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class CustomUserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserPasswordResetForm(SetPasswordForm):
    """
    A form that lets a user change set their password without entering the old
    password
    """

    new_password1 = forms.CharField(
        widget=forms.PasswordInput,
        strip=False,
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs['user']
        super(CustomUserPasswordResetForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    PASSWORD_MISSMATCH,
                    code='password_mismatch',
                )
            ValidationUser.password_validation(password2)

        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
