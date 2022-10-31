from django.shortcuts import render
from forms import RegistrationUser

def register(request):
    form = RegistrationUser()
    return render(request, 'users/registration.html', { 'form': form })
