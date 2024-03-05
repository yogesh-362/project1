from django.urls import path, include
from app3 import views
from rest_framework.routers import DefaultRouter
# from app3.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('stuapi', views.StudentModelViewSet, basename='student'),

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify_token'),
]
