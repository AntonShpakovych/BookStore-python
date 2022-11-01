from django.urls import path
from shop import views


urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('books/', views.books,  name = 'books'),
    path('books/<int:id>/', views.book, name = 'book')
]
