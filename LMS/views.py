from django.shortcuts import render
from main.models import HomeBookCarousel


def index(request):
    images = HomeBookCarousel.objects.all()
    context = {
        "slider_images" : images
    }
    return render(request, 'index.html', context)


def login_view(request):
    return render(request, 'logInForm.html')


def signup_view(request):
    return render(request, 'studentInformationForm.html')