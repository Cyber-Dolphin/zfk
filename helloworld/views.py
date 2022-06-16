from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'helloworld/index.html', {'title': 'Новости', 'tasks': tasks})


def enrollee(request):
    return render(request, 'helloworld/enrollee.html')


def student(request):
    return render(request, 'helloworld/student.html')


def graduate(request):
    return render(request, 'helloworld/graduate.html')


def timetable(request):
    return render(request, 'helloworld/timetable.html')


def schedule(request):
    return render(request, 'helloworld/schedule.html')


def scholarship(request):
    return render(request, 'helloworld/scholarship.html')


def studentlife(request):
    return render(request, 'helloworld/studentlife.html')


def basetostudent(request):
    return render(request, 'helloworld/basetostudent.html')


def teachers(requst):
    return render(requst, 'helloworld/teachers.html')