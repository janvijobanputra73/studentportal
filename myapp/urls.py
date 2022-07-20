from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.index),
    path('about/',views.about,name='about'),
    path('contact/',views.contact),
    path('userlogout/',views.userlogout),
    path('h1/',views.h1),
    path('myprofile/',views.myprofile),
    
    #for student
    path('student_home/',views.student_home, name="student_home"),


    #for staff
    path('staff_home/', views.staff_home, name="staff_home"),


    #for hod
    path('hod_home/', views.hod_home, name="hod_home"),
    path('deletedata/<int:id>', views.deletedata, name="deletedata"),
   
]

