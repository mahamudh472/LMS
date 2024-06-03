from django.urls import path

from . import views

app_name = 'librarian'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('manage_book/', views.manage_book, name='manage_book'),
]