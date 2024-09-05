from django.contrib import admin
from main.models import Category, Book, HomeBookCarousel, BookRequest, Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(HomeBookCarousel)
admin.site.register(BookRequest)
admin.site.register(Comment)
