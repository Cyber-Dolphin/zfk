from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('enrollee', views.enrollee, name='enrollee'),
    path('student', views.student, name='student'),
    path('graduate', views.graduate, name='graduate'),
    path('timetable', views.timetable, name='timetable'),
    path('schedule', views.schedule, name='schedule'),
    path('scholarship', views.scholarship, name='scholarship'),
    path('studentlife', views.studentlife, name='studentlife'),
    path('basetostudent', views.basetostudent, name='basetostudent'),
    path('teachers', views.teachers, name='teachers'),
]
