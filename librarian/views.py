import random

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils import timezone

from LMS import settings
from main.models import Book, BookRequest, OtpVerification, Category
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import StudentProfile
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
# Create your views here.

@staff_member_required
def dashboard(request):
    total_students = StudentProfile.objects.all().count()
    total_books = Book.objects.all().count()
    total_categories = Category.objects.all().count()
    issued_books = BookRequest.objects.filter(status="accepted").count()
    context = {
        "total_students": total_students,
        "total_books": total_books,
        "total_categories": total_categories,
        "issued_books": issued_books
    }
    return render(request, 'librarian/index.html', context)
@staff_member_required
def students(request):
    student_list = StudentProfile.objects.all()
    paginator = Paginator(student_list, 10)
    return render(request, 'librarian/studentList.html', {'students': student_list})
@staff_member_required
def manage_book(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)

    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    context = {
        'books': page_obj,
    }
    return render(request, 'librarian/manageBooks.html', context)

@staff_member_required
def book_requests(request):
    book_request_list = BookRequest.objects.order_by('-id')
    context = {
        'requests': book_request_list,
        "status" : BookRequest.STATUS_OPTIONS,
    }
    return render(request, 'librarian/bookRequests.html', context)

@staff_member_required
def accept_request(request, id):
    book_req = BookRequest.objects.get(id=id)
    book_req.status = "accepted"
    book_req.save()

    otp = random.randint(100000, 999999)
    otpVerification = OtpVerification.objects.create(
        user=book_req.student,
        req=book_req,
        otp=otp,
    )
    otpVerification.send_at = timezone.now()
    otpVerification.save()

    # send otp
    name = book_req.student.name
    email = book_req.student.user.email
    template = render_to_string(
        'otp_email.html',
        {'name': name, 'otp': otp, 'action': "Book verification", 'book_name': book_req.book.title}
    )
    send_mail(
        'Otp for confirm Book',
        template,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        html_message=template
    )

    return redirect("librarian:book_requests")

@staff_member_required
def book_tracking(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        query_otp = OtpVerification.objects.filter(otp=otp).first()

        if query_otp:
            book_request = query_otp.req
            return render(request, 'librarian/bookTracking.html', {"book_req": book_request})
        else:
            messages.warning(request, "No book records found")
            return redirect("librarian:dashboard")

@staff_member_required
def issue_book(request, req_id):
    book_req = BookRequest.objects.get(id=req_id)
    book_req.status = "received"
    book_req.issue_date = timezone.now()
    book_req.return_date = timezone.now() + timezone.timedelta(days=book_req.book_time)
    book_req.save()

    return redirect('librarian:book_requests')

@staff_member_required()
def return_book(request, req_id):
    book_req =  BookRequest.objects.get(id=req_id)
    book_req.status = "returned"
    book_req.save()

    return redirect('librarian:book_requests')

@staff_member_required
def active_student(request, student_id):
    student = StudentProfile.objects.get(id=student_id)
    student.is_active = True
    student.save()
    return redirect("librarian:students")


@staff_member_required
def update_book_info(request):
    if request.method == "POST":
        main_id = request.POST.get("id", None)
        if main_id:
            obj = Book.objects.get(id=main_id)
        else:
            obj = Book()

        obj.title = request.POST.get("title")
        obj.author = request.POST.get("author")
        obj.desc = request.POST.get("desc")
        obj.pages = request.POST.get("pages")
        obj.count = request.POST.get("count")
        obj.book_id = request.POST.get("book_id")
        obj.issued = request.POST.get("issued")

        # Handle category
        category_name = request.POST.get("category")
        cat = Category.objects.filter(name__icontains=category_name).first()
        if cat:
            obj.category = cat
        else:
            obj.category = Category.objects.create(name=category_name, desc="default")

        # Handle image upload
        image = request.FILES.get("image")
        if image:
            obj.image = image

        # Save the updated book object
        obj.save()

        return redirect("librarian:manage_book")


