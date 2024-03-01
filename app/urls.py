from django.urls import path
from .views import stu_api
from app import views
from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    # # path('stuinfo/<int:pk>/', student_detail, name='stuinfo'),
    # # path('stulist/', student_list, name='stulist'),
    # path('stuapi/', stu_api, name='stuapi'),
    path('stuAPI/',views.StudentAPI.as_view(), name='stuAPI'),
]



# While using Postman
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from app import views
#
# router = DefaultRouter()
# router.register('stud', views.StudentViewSet, basename="stud")
#
# urlpatterns = [
#     path('', include(router.urls))
#     ]
