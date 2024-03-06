from django.urls import path
# from .views import stu_api
from app import views
from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('stuapi/', views.StudentList.as_view()),
]



