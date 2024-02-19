from django.shortcuts import render
from main.models import Category, Book
# Create your views here.
def book_by_category(request, category):
    books = Book.objects.filter(category=category)

    return render(request, "singlecata.html", {"books": books})

def temp(request):
    return render(request, "singlecata.html")