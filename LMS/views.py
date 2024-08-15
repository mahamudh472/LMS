from django.shortcuts import render
from main.models import HomeBookCarousel, Book


def index(request):
    images = HomeBookCarousel.objects.all()
    if Book.objects.count() > 10:
        books = Book.objects.order_by("?")[:10]
    else:
        books = Book.objects.all()
    context = {
        "slider_images" : images,
        "books": books
    }
    return render(request, 'index.html', context)


def login_view(request):
    return render(request, 'logInForm.html')


def signup_view(request):
    return render(request, 'studentInformationForm.html')