from django.urls import path
from . import views
urlpatterns = [
    path("book_by_category/<str:category>", views.book_by_category, name="book_by_catagory"),

]