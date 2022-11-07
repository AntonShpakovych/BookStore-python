from django.shortcuts import render, get_object_or_404
from shop.models import Book
from shop.services.books_service import BooksService


def home_page(request):
    return render(request, 'pages/home.html')



def books(request):
    current_filter, current_sorter, sorters, filters, page_obj = BooksService(request).call()
    books_count = Book.objects.all().count()

    return render(request, 'shop/pages/books.html', { 'page_obj': page_obj,
                                                      'filters': filters,
                                                      'books_count': books_count,
                                                      'current_filter': current_filter,
                                                      'current_sorter': current_sorter,
                                                      'sorters': sorters
                                                        })

def book(request, id):
    book = get_object_or_404(Book, id = id)

    return render(request, 'shop/pages/book.html', { 'book': book })
