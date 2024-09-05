from django.db import models
from autoslug import AutoSlugField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, blank=True)
    author = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    image = models.ImageField(upload_to='books', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True, default=1)
    book_id = models.CharField(max_length=20, blank=True, null=True)
    issued = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def is_avail(self):
        if self.count > 0:
            return True
        else:
            return False

    def available(self):
        return self.count - self.issued


class HomeBookCarousel(models.Model):
    image = models.ImageField(upload_to="Book_carousel", blank=True, null=True)


class BookRequest(models.Model):
    STATUS_OPTIONS = {
        "pending": "Pending",
        "accepted": "Accepted",
        "rejected": "Rejected",
        "received": "Received",
        "returned": "Returned"
    }
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, blank=True, null=True)
    book_time = models.IntegerField(default=0)
    issue_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} - {self.student.user.username}"


class OtpVerification(models.Model):
    user = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    req = models.ForeignKey('main.BookRequest', on_delete=models.CASCADE, null=True)
    otp = models.CharField(max_length=10)
    send_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)


class WishList(models.Model):
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    book = models.ForeignKey('main.Book', on_delete=models.CASCADE)
    add_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE)
    book = models.ForeignKey('main.Book', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True )
    add_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)