
from django.urls import path
from app2 import views

urlpatterns = [

    # for seperate classes
    # # path('stuapi/', views.StudentCreate.as_view(), name="hw"),
    # # path('stuapi/<int:pk>/', views.StudentRetrieve.as_view()),
    # # path('stuapi/<int:pk>/',views.StudentAPI.as_view()),
    # # path('stuapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('stuapi/<int:pk>/', views.StudentDelete.as_view()),

    # for group of classes
    # path('stuapi/', views.LCStudent.as_view(), name="hw"),
    # path('stuapi/<int:pk>/', views.UDRStudent.as_view()),

    # Using Concrete API views(Separate)
    # path('stuapi/', views.StudentList.as_view()),
    # path('stuapi/', views.StudentCreate.as_view()),
    # path('stuapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('stuapi/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('stuapi/<int:pk>/', views.StudentDestroy.as_view()),

    # using Concrete API view(Combination)
    #   path('stuapi/', views.StudentListCreate.as_view()),
    # path('stuapi/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    #   path('stuapi/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
    #   path('stuapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view())

]