from django.urls import path
from app3 import views

urlpatterns = [
    # Using Concrete API views(Separate)
    path('stuapi/', views.StudentList.as_view()),
    # path('stuapi/', views.StudentCreate.as_view()),
    # path('stuapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('stuapi/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('stuapi/<int:pk>/', views.StudentDestroy.as_view()),
]
