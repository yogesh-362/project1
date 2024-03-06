from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .mypaginations import MyPageNumberPagination
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination



