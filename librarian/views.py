from django.shortcuts import render
from main.models import Book

# Create your views here.

def dashboard(request):
    return render(request, 'librarian/index.html')

def students(request):
    return render(request, 'librarian/studentList.html')

def manage_book(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'librarian/manageBooks.html', context)