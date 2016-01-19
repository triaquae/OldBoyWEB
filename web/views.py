from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'web/index.html')


def course_py_devops(request):
    return render(request,'web/course_py_devops.html')