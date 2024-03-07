from django.urls import path, include
from app import views
from rest_framework.routers import DefaultRouter
# from app3.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('singer', views.SingerViewSet, basename='singer'),
router.register('song', views.SongViewSet, basename='song'),

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))

]