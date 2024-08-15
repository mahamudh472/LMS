from django.contrib import admin
from main.models import Category, Book, HomeBookCarousel, BookRequest
# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(HomeBookCarousel)
admin.site.register(BookRequest)
