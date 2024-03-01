from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from  rest_framework.parsers import JSONParser
import  io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# # only for One Student
# def student_detail(request, pk):
#     stu = Student.objects.get(id=pk)
#     serializer = StudentSerializer(stu)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data) # you can use this line instead of above two line in all if statements below
#
#
# # QuerySet : For All Students
# def student_list(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu, many=True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data, safe=False)
#
# @csrf_exempt
def stu_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id  = python_data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    # Update data all not to write partial=True
    # Update only part of dara use partial = True
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id  = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Delete!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
#


# While Using Postman
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse,JsonResponse
# from rest_framework.viewsets import ModelViewSet
#
#
# class StudentViewSet(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



# using Class Based View
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = StudentSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Updated!!'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg': 'Data Delete!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')


