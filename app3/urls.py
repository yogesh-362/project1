from django.urls import path, include
from app3 import views
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
#
# router.register('stuapi', views.StudentModelViewSet, basename='student'),

urlpatterns = [
    # path('',include(router.urls)),
    # path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('stuapi/',views.student_api),
    path('stuapi/<int:pk>/',views.student_api)
]