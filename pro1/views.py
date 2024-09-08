from django.shortcuts import render,redirect
from . models import *

def index(request):
    return render(request,'index.html')
def regdata(request):
    if request.method=="POST":
        userphoto=request.FILES['userphoto']
        username=request.POST.get('username')
        useremail=request.POST.get('useremail')
        usermobile=request.POST.get('usermobile')
        userpassword=request.POST.get('userpassword')
        db=details(photo=userphoto,name=username,email=useremail,mobile=usermobile,password=userpassword)
        db.save()
    return render(request,'regform.html')
def userview(request):
    data=details.objects.all()
    return render(request,'userlist.html',{'result':data})
def login(request):
    return render(request,'login.html')

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['adminemail'] = email
        request.session['admin'] ='admin'
        return render(request,'index.html',{'status': 'admin login successfull'} )

    elif details.objects.filter(email=email,password=password).exists():
        udet=details.objects.get(email=request.POST['email'],password=password)
        if udet.password == request.POST['password']:
            request.session['uid'] = udet.id
            request.session['uname'] = udet.name
            request.session['uemail'] = email
            request.session['user'] = 'user'
            return render(request,'index.html',{'status': 'user login successfull'})

    else:
            return render(request, 'login.html', {'status': 'incorrect credentials'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

 

