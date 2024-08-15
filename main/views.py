import random


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils import timezone

from LMS import settings
from accounts.models import StudentProfile
from main.models import Category, Book, BookRequest, OtpVerification, WishList
from django.core.mail import send_mail


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
    book_holders = book.bookrequest_set.filter(status="received")
    return render(request, "readBooks.html", {"book": book, "book_holders": book_holders})


def add_to_wishlist(request, book_id):
    book = Book.objects.get(id=book_id)
    if WishList.objects.filter(student=request.user.studentprofile, book=book):
        messages.warning(request, "Already in wishlist.")
        return redirect("/")
    WishList.objects.get_or_create(
        student=request.user.studentprofile,
        book=book,
    )
    messages.success(request, "Book added to wishlist.")
    return redirect("/")

def remove_from_wishlist(request, book_id):
    book = Book.objects.get(id=book_id)
    if WishList.objects.filter(student=request.user.studentprofile, book=book).exists():
        request.user.studentprofile.wishlist_set.filter(book=book)[0].delete()
        messages.warning(request, "Book removed from wishlist")
    return redirect("/")


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

@login_required(login_url='accounts:login')
def student_information(request):
    if request.method == 'POST':
        # Extract the form data
        data = {
            'shift': request.POST.get('shift'),
            'department': request.POST.get('department'),
            'name_bangla': request.POST.get('name_bangla'),
            'name': request.POST.get('name'),
            'father_name': request.POST.get('father_name'),
            'mother_name': request.POST.get('mother_name'),
            'address': request.POST.get('address'),
            'post_office': request.POST.get('post_office'),
            'upazila': request.POST.get('upazila'),
            'district': request.POST.get('district'),
            'number': request.POST.get('number'),
            'parent_number': request.POST.get('parent_number'),
            'blood_group': request.POST.get('blood_group'),
            'technology_code': request.POST.get('technology_code'),
            'semester': request.POST.get('semester'),
            'birth_date': request.POST.get('birth_date'),
            'ssc_roll': request.POST.get('ssc_roll'),
            'policy_agreement': request.POST.get('policy_agreement') == 'on',
        }

        # Handle file uploads
        if 'image' in request.FILES:
            data['image'] = request.FILES['image']
        if 'signature' in request.FILES:
            data['signature'] = request.FILES['signature']
        if 'parent_signature' in request.FILES:
            data['parent_signature'] = request.FILES['parent_signature']

        # Update or create the StudentProfile object
        profile, created = StudentProfile.objects.update_or_create(
            user=request.user,
            defaults=data
        )

        if created:
            message = "Profile created successfully."
        else:
            message = "Profile updated successfully."

        return redirect('index')  # Redirect to the same page
    else:
        try:
            profile = StudentProfile.objects.get(user=request.user)
            return render(request, 'studentInformationForm.html', {'profile': profile})
        except StudentProfile.DoesNotExist:
            return render(request, 'studentInformationForm.html')


def request_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        days = request.POST.get("days")
        book = Book.objects.get(pk=int(book_id))

        # Check for existing requests for this book by this user
        existing_request = request.user.studentprofile.bookrequest_set.filter(book=book).exclude(
            status="rejected").first()

        if existing_request:
            if existing_request.status == "pending":
                messages.warning(request, "You already have a pending request for this book.")
            else:
                messages.warning(request, "You have already requested this book.")
            return redirect('main:book', book_id=book.id)

        # Create a new book request
        BookRequest.objects.create(book=book, student=request.user.studentprofile, book_time=days, status="pending")
        messages.success(request, "Book request added successfully.")


        return redirect('main:book', book_id=book.id)
