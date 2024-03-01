from django.urls import path
from app1 import views

urlpatterns = [
    path('stuAPI/', views.StudentAPI.as_view(), name='stuAPI'),
]
