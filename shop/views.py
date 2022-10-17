"""Shop logic"""
from django.shortcuts import render


def home_page(request):
    """Render home page"""
    return render(request, 'shop/pages/home.html')
