from django.urls import path, include
from app4 import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('stuapi', views.StudentViewSet, basename='student'),

urlpatterns = [
    path('',include(router.urls)),
]