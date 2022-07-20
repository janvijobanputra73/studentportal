
from dataclasses import fields
from django import forms


from .models import hod, staff, student,usersignup,about,contactinfo

class usersignupform(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'
        
class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"        

class staffform(forms.ModelForm):
    class Meta:
        model=staff
        fields="__all__"     
        
class hodform(forms.ModelForm):
    class Meta:
        model=hod
        fields="__all__"  

class aboutform(forms.ModelForm):
    class Meta:
        model=about
        fields="__all__"
        
class contactform(forms.ModelForm):
    class Meta:
        model=contactinfo
        fields="__all__"                         
