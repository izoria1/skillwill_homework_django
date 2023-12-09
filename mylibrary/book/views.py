from django.shortcuts import render
from .models import Book

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book/detail.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})
