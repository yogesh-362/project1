from django.urls import path, include
from app3 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# from app3.auth import CustomAuthToken

router = DefaultRouter()

router.register('stuapi', views.StudentModelViewSet, basename='student'),

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/', CustomAuthToken.as_view())
]
