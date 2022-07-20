
from django.db import models

# Create your models here.


class usersignup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()
    role=models.CharField(max_length=20,default="")
    
class student(models.Model):
    stname=models.CharField(max_length=20,default="")
    lastname=models.CharField(max_length=20,default="")
    ststd=models.CharField(max_length=20,default="")
    stcity=models.CharField(max_length=20,default="")
    state=models.CharField(max_length=20,default="")
    enrno=models.CharField(max_length=20,default="")
    zipcode=models.CharField(max_length=20,default="")
    stphoto=models.FileField(upload_to="photoupload",default="")
    
class staff(models.Model):
    stafffn=models.CharField(max_length=20,default="")
    staffln=models.CharField(max_length=20,default="")
    staffsub=models.CharField(max_length=20,default="")
    staffstd=models.CharField(max_length=20,default="")
    staffcity=models.CharField(max_length=20,default="")
    staffphoto=models.FileField(upload_to="staffimag",default="")
    phno=models.BigIntegerField(default="")
    address=models.CharField(max_length=20,default="")
    experience=models.CharField(max_length=3,default="")
    
class hod(models.Model):
    hodnm=models.CharField(max_length=20,default="")
    
class about(models.Model):
    feedback=models.TextField(max_length=200,default="")    
            
class contactinfo(models.Model):
    name=models.CharField(max_length=20,default="")
    email=models.EmailField(default="")
    subject=models.CharField(max_length=20,default="")
    message=models.TextField(max_length=200,default="")            
