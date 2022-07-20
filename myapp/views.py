
from django.shortcuts import redirect, render
from .forms import studentform, usersignupform,aboutform,contactform,staffform
from .models import student, usersignup,staff
from django.contrib.auth import logout
from django.core.mail import send_mail
from studentportal import settings


# Create your views here.

def userregi(request):
    rol=request.POST['role']
    myfrm=usersignupform(request.POST)
    if myfrm.is_valid():
        myfrm.save()
        print("signup successfully!")
        request.session['userrole']=rol
        
        #sending mail
        
        
        sub="successfully done!"
        msg="hello,signup seccssfully!!!"
        from_id=settings.EMAIL_HOST_USER
        #to_id=['akbariprince326@gmail.com',"janvijobanputra08@gmail.com"]
        to_id=[request.POST["username"]]
        send_mail(sub,msg,from_id,to_id)
        
        
        return redirect('/')
    else:
        print(usersignupform.errors)
    
def userlogin(request):
    
    unm=request.POST['username']
    pas=request.POST['password']
    rol=request.POST['role']
    userID=usersignup.objects.get(username=unm)
    print("userID:",userID.id)
    userauth=usersignup.objects.filter(username=unm,password=pas,role=rol)
    if userauth:
        print("Login Suucess!")
        request.session['userrole']=rol
        request.session["userid"]=userID.id
    else:
        print("Error...Login fail!")
    


def index(request):
    user=request.session.get('userrole') 
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            userregi(request)
            if request.session.get('userrole')=='student':
                
                return redirect('student_home')
            if request.session.get('userrole')=='staff':
                return redirect('staff_home')
            if request.session.get('userrole')=='hod':
                return redirect('hod_home')
        
            
        elif request.POST.get("login")=="login":
            userlogin(request)
            if request.session.get('userrole')=='student':
                return redirect('student_home')
            if request.session.get('userrole')=='staff':
                return redirect('staff_home')
            if request.session.get('userrole')=='hod':
                return redirect('hod_home')
            
    return render(request,'index.html',{'user':user})   

"""def myprofile(request,id):
    user=request.session.get('userrole')
    userid=request.session.get('userid')
    stid=usersignup.objects.get(id=id)
    
    if request.method=='POST':
        userupdate=usersignupform(request.POST)    
        if userupdate.is_valid():
            userupdate=usersignupform(request.POST,instance=stid)
            userupdate.save()
            print("updated!!")
            return redirect("/")
        else:
            print(userupdate.errors)
    #return render(request,'profile.html',{'user':user,'userid': usersignup.objects.get(id=id)})
    return render(request,'myprofile.html')
"""

def myprofile(request):
    user=request.session.get('userrole')
    userid=request.session.get('userid')
    id=usersignup.objects.get(id=userid)
    if request.method=='POST':
        userupdate=usersignupform(request.POST)
        if userupdate.is_valid():
            userupdate=usersignupform(request.POST,instance=id)
            userupdate.save()
            print("upadated!!")
            return redirect("/")
        else:
            print(userupdate.errors)
    return render(request,'myprofile.html',{'user':user,'userid':usersignup.objects.get(id=userid)})

def contact(request):
    user=request.session.get('userrole')
    if request.method=="POST":
        contactdata=contactform(request.POST)
        if contactdata.is_valid():
            contactdata.save()
            print("feedback has  been uploaded!")
        else:
            print(contactdata.errors)    
        return redirect(index)
    return render(request,'contact.html',{'user':user})

def about(request):
    user=request.session.get('userrole')
    if request.method=="POST":
        feedbackupload=aboutform(request.POST)
        if feedbackupload.is_valid():
            feedbackupload.save()
            print("feedback has  been uploaded!")
        else:
            print(feedbackupload.errors)    
        return redirect(index)
    return render(request,'about.html',{'user':user})

def userlogout(requset):
    logout(requset)
    return redirect("/")


def student_home(request):
    if request.method=="POST":
        stdataupload=studentform(request.POST,request.FILES)
        if stdataupload.is_valid():
            stdataupload.save()
            print("data has  been uploaded!")
        else:
            print(stdataupload.errors)    
        return redirect(index)  
      
    return render(request,"student_home.html")

def staff_home(request):
    if request.method=="POST":
        staffdata=staffform(request.POST,request.FILES)
        if staffdata.is_valid():
            staffdata.save()
            print("data has  been uploaded!")
        else:
            print(staffdata.errors)    
        return redirect(index)
    return render(request,"staff_home.html")

def hod_home(request):
    stdata=usersignup.objects.all()
    studdata=student.objects.all()
    staffdata=staff.objects.all()
    return render(request,"hod_home.html",{"stdata":stdata,'studdata':studdata,'staffdata':staffdata})


def deletedata(request,id):
    stid=usersignup.objects.get(id=id)
    usersignup.delete(stid)
    return redirect("hod_home")


def h1(request):
    return render(request,"h1.html")




