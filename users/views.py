from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import BadHeaderError

from users.forms import CustomUserCreationForm, CustomUserLoginForm, BillingAddressForm, ShippingAddressForm
from users.models import CustomUser
from users.messages.information_messages import SIGN_IN, INVALID_SIGN_IN, SIGN_UP, INVALID_HEADER
from users.services.user_mail_service import UserMailService
from users.services.user_address_create_or_update import UserAddressCreateOrUpdate


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(request, messages.SUCCESS, SIGN_UP)
            return redirect('home')

        return render(request, 'users/pages/sign_up.html', { 'form': form })

    form = CustomUserCreationForm()
    return render(request, 'users/pages/sign_up.html', { 'form': form })

def log_out(request):
    logout(request)
    return redirect('home')

def sign_in(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email = cd['email'], password = cd['password'])
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, SIGN_IN)
                return redirect('home')
            else:
                return render(request, 'users/pages/sign_in.html', {'form': form, 'errors': INVALID_SIGN_IN})
    form = CustomUserLoginForm()
    return render(request, 'users/pages/sign_in.html', {'form': form })

def password_reset_request(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_user = CustomUser.objects.get(email=data)
            if associated_user:
                user_mail_service = UserMailService()
                try:
                    user_mail_service.call(associated_user)
                except BadHeaderError:
                    messages.add_message(request, messages.ERROR, INVALID_HEADER)
                    return redirect('password_reset')
                return redirect ("password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(request, 'users/pages/password_reset.html', {'form': password_reset_form})

def settings(request):
    user = request.user

    if request.method == 'POST':
        type = request.POST.get('type')
        user_address_service = UserAddressCreateOrUpdate(user, type, request.POST)
        user_address_service.call()

        if user_address_service.is_billing():
            billing_address_form = user_address_service.active_form
            shipping_address_form = user_address_service.dormant_form
        else:
            billing_address_form = user_address_service.dormant_form
            shipping_address_form = user_address_service.active_form
    else:    
        billing_address_form = BillingAddressForm(instance=user.billing_address)
        shipping_address_form = ShippingAddressForm(instance=user.shipping_address)
   
    return render(request, 'users/pages/settings.html', {'billing_form': billing_address_form, 'shipping_form': shipping_address_form})
