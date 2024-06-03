from django.urls import path
from . import views
urlpatterns = [
    path("book_by_category/<str:category>", views.book_by_category, name="book_by_category"),
    path("search", views.search, name="search"),
    path("book/<int:book_id>", views.book, name="book"),
    path("all_categories", views.all_categories, name="all_categories"),
    path("student-information", views.student_information, name="student-information")

]
