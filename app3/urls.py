from django.urls import path, include
from app3 import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('stuapi', views.StudentReadOnlyModelViewSet, basename='student'),

urlpatterns = [
    path('',include(router.urls)),
]