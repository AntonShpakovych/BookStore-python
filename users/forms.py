from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from users.messages import validation_messages
from django.contrib.auth.hashers import check_password

import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code

from users.models import CustomUser, BillingAddress, ShippingAddress
from users.validation import ValidationUser


class BillingAddressForm(forms.ModelForm):
    first_name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter first name', 'class':'form-control'}))
    last_name = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter last name', 'class':'form-control'}))
    city = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter city', 'class':'form-control'}))
    country = CountryField(blank_label='Select country',).formfield(
        widget=CountrySelectWidget(
           attrs={'class': 'form-control'}
        )
    )
    phone = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter phone', 'class':'form-control'}))
    zip = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter zip', 'class':'form-control'}))
    address = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter address', 'class':'form-control'}))

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
                    validation_messages.PASSWORD_MISSMATCH,
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


class CustomUserChangeEmailForm(forms.Form):
    email = forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter email', 'class':'form-control'}))
    def set_user(self, user):
        self.user = user

    def clean(self):
        new_email = self.cleaned_data['email']
        if new_email:
            if CustomUser.objects.filter(email=new_email):
                raise ValidationError({'email': validation_messages.INVALID_EMAIL})
            ValidationUser.email_validation(new_email)
        else:
            raise ValidationError({'email': validation_messages.EMPTY_EMAIL})

        return self.cleaned_data

    def save(self, commit=True):
        email = self.cleaned_data["email"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user

class CustomUserChangePasswordForm(forms.Form):
    """
    A form that lets a user change set their password with entering the old
    password
    """

    old_password = forms.CharField(widget= forms.PasswordInput
                                  (attrs={'placeholder':'Enter old password', 'class':'form-control'}))
    new_password1 = forms.CharField(widget= forms.PasswordInput
                                   (attrs={'placeholder':'Enter new password', 'class':'form-control'}))
    new_password2 = forms.CharField(widget= forms.PasswordInput
                                    (attrs={'placeholder':'Enter confirm password   ', 'class':'form-control'}))

    def set_user(self, user):
        self.user = user

    def clean(self):
        old_password = self.cleaned_data['old_password']
        
        
        if check_password(old_password, self.user.password):
            password1 = self.cleaned_data['new_password1']
            password2 = self.cleaned_data['new_password2']

            if password1 and password2:
                if password1 != password2:
                    raise forms.ValidationError({'new_password2': validation_messages.PASSWORD_MISSMATCH})
            ValidationUser.password_validation(password2, sign_up=False)
            return self.cleaned_data 
        else:
            raise forms.ValidationError({'old_password':validation_messages.OLD_PASSWORD_DOESNT_EXIST})
    
    def save(self, commit=True):
        password = self.cleaned_data["new_password2"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
