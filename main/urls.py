from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("book_by_category/<str:category>", views.book_by_category, name="book_by_category"),
    path("search", views.search, name="search"),
    path("book/<int:book_id>", views.book, name="book"),
    path("all_categories", views.all_categories, name="all_categories"),
    path("student-information", views.student_information, name="student_information"),
    path('request-book/', views.request_book, name='request_book'),
    path('add_to_wishlist/<int:book_id>', views.add_to_wishlist, name="add_to_wishlist"),
    path('remove_from_wishlist/<int:book_id>', views.remove_from_wishlist, name="remove_from_wishlist"),
    path('add_comment/', views.add_comment, name="add_comment")

]
