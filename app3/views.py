from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .customauth import CustomAuthentication
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # For Local Authentication and Global inside settings.py
    authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
