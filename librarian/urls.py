from django.urls import path

from . import views

app_name = 'librarian'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('manage_book/', views.manage_book, name='manage_book'),
    path('book_requests/', views.book_requests, name='book_requests'),
    path('accept_req/<int:id>', views.accept_request, name="accept_request"),
    path('book_tracking/', views.book_tracking, name="book_tracking"),
    path('issue_book/<int:req_id>', views.issue_book, name="issue_book"),
    path('return_book/<int:req_id>', views.return_book, name="return_book"),
    path('active_student/<int:student_id>', views.active_student, name="active_student"),
    path('update_book_info/', views.update_book_info, name="update_book_info"),
    path('remove_book/<int:book_id>', views.remove_book, name="remove_book"),
    path('comments/', views.comments, name="comments")

]