from django.urls import path
from app3 import views
urlpatterns = [
    path('stuapi/', views.StudentListCreate.as_view()),
    path('stuapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]