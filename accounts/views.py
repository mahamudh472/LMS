from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("index"))

    return render(request, 'logInForm.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username).exists():
            return redirect("accounts:login")
        elif password == password2:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse("index"))

    return render(request, 'signupForm.html')


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))
