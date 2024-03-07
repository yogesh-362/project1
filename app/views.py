from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
     if request.method == 'POST':
       fm = StudentRegistration(request.POST)
       if fm.is_valid():
           fm.save()
     else:
         fm = StudentRegistration()
     stu = User.objects.all()     

     return render(request, 'app/addandshow.html', {"form":fm,'stu':stu})

def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")

def update_data(request, id):
     if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
     else:
         pi = User.objects.get(pk=id)
         fm = StudentRegistration(instance=pi)
     return render(request, 'app/updatestudent.html',{"form":fm})

def setcookie(request):
    response = render(request, 'app/setcookie.html') # object creating
    response.set_cookie('name', 'Soham', max_age=60)#max_age in seconds cookie deleted automatically in this time
    return response

def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name', "guest") # other method , guest print if key doesn't exit
    return render(request, 'app/getcookie.html',{"name":name})

def delcookie(request):
    response = render(request, 'app/delcookie.html') # Creating object
    response.delete_cookie('name')
    return response


def main(request):
    if request.method == 'POST':
        file = request.FILES['file']
        FILE.objects.create