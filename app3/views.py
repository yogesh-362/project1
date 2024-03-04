from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # For Local Authentication and Global inside settings.py
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser] #if staff is checked
    # permission_classes = [IsAuthenticatedOrReadOnly] # anonymous user can only see data
    # permission_classes = [DjangoModelPermissions] # More powerfull And Give permissions explicitly through backend means from database
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly] # only see data for anonymous user
