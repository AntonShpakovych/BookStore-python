from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from users.messages import validation_messages

import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code

from users.models import CustomUser, BillingAddress, ShippingAddress
from users.messages.validation_messages import PASSWORD_MISSMATCH
from users.validation import ValidationUser


class BillingAddressForm(forms.ModelForm):
    first_name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your first name', 'required': True, 'class':'form-control'}))
    last_name = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your last name', 'required': True, 'class':'form-control'}))
    phone = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your phone', 'required': True, 'class':'form-control'}))
    city = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your city', 'required': True, 'class':'form-control'}))
    country = CountryField(blank_label='Select country',).formfield(
        widget=CountrySelectWidget(
           attrs={'class': 'form-control'}
        )
    )
    zip = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your zip', 'required': True, 'class':'form-control'}))
    address = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your address', 'required': True, 'class':'form-control'}))

    class Meta:
        model = BillingAddress
        fields = "__all__"
    
    def clean(self):
        cleaned_data = super(BillingAddressForm, self).clean()
        
        try:
            pn = phonenumbers.parse(cleaned_data.get('phone'))
            if not cleaned_data.get('country') == region_code_for_country_code(pn.country_code):
                self.add_error('phone', validation_messages.ADDRESS_PHONE)
        except phonenumbers.NumberParseException:
            self.add_error('phone', validation_messages.ADDRESS_PHONE)

class ShippingAddressForm(BillingAddressForm):
    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args,**kwargs)
    
    class Meta(BillingAddressForm.Meta):
        model = ShippingAddress
        fields = BillingAddressForm.Meta.fields

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
