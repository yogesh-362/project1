from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import DestroyAPIView
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Ordering Filter
    filter_backends = [OrderingFilter]
    ordering_fields = ['name'] # for specific fields if you don't write then all filter are display on browser in filter button




