from django.shortcuts import render
from main.models import Category, Book


# Create your views here.
def book_by_category(request, category):
    books = Book.objects.filter(category__name=category)

    return render(request, "singlecata.html", {"books": books, "category": category})


def search(request):
    if request.method == "GET":
        text = request.GET.get("search_text")
        books = Book.objects.filter(title__icontains=text) | Book.objects.filter(
            author__icontains=text) | Book.objects.filter(category__name__icontains=text) | Book.objects.filter(
            desc__icontains=text)
        return render(request, "singlecata.html",
                      {"books": books, "text": text, "count": books.count(), "operation": "search"})


def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "readBooks.html", {"book": book})


def all_categories(request):
    categories = Category.objects.all()
    # books by categories
    context = {
        "categories": categories,

    }
    for category in categories:
        books = Book.objects.filter(category__name=category.name)
        context[category.name] = books

    return render(request, "allcata.html", context)


def student_information(request):
    return render(request, "studentInformationForm.html")
