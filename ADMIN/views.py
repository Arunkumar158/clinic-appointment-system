from django.shortcuts import render,redirect
from . models import *

# Create your views here.

def add_doctor(request):
    if request.method=="POST":
        doctorphoto = request.FILES['doctorphoto']
        doctorname = request.POST.get('doctorname')
        doctoremail = request.POST.get('doctoremail')
        # doctorphone = request.POST.get('doctorphone')
        doctorqualification = request.POST.get('doctorqualification')
        enterdutystarttime = request.POST.get('enterdutystarttime')
        # enterdutyendtime = request.POST.get('enterdutyendtime')
        anysuggestion = request.POST.get('anysuggestions')
        doct_db = doctorlist(doctorphoto=doctorphoto,doctorname=doctorname,doctoremail=doctoremail,doctorqualification=doctorqualification,enterdutystarttime=enterdutystarttime,anysuggestion=anysuggestion,)
        doct_db.save()
    return render(request,'add_doctor.html')

def doctor_list(request):
    doctor_data = doctorlist.objects.all()
    return render(request,'doctorlist.html',{'result':doctor_data})

def doc_delete(request,id):
    data=doctorlist.objects.get(pk=id)
    data.delete()
    return redirect(doctor_list)

def doc_update(request,id):
    data=doctorlist.objects.get(pk=id)
    return render(request,'update_doctor.html',{'result':data})

def doc_updates(request,id):
    if request.method=="POST":
        doctorphoto = request.FILES['doctorphoto']
        doctorname = request.POST.get('doctorname')
        doctoremail = request.POST.get('doctoremail')
        # doctorphone = request.POST.get('doctorphone')
        doctorqualification = request.POST.get('doctorqualification')
        enterdutystarttime = request.POST.get('enterdutystarttime')
        # enterdutyendtime = request.POST.get('enterdutyendtime')
        anysuggestion = request.POST.get('anysuggestions')
        doct_db = doctorlist(id=id,doctorphoto=doctorphoto,doctorname=doctorname,doctoremail=doctoremail,doctorqualification=doctorqualification,enterdutystarttime=enterdutystarttime,anysuggestion=anysuggestion,)
        doct_db.save()
        
        return redirect(doctor_list)
    return render(request,'update_doctor.html')


def regdata(request):
    if request.method=="POST":
        userphoto=request.FILES["userphoto"]
        username=request.POST.get("username")
        useremail=request.POST.get("useremail")
        userphone=request.POST.get("usermobile")
        userpassword=request.POST.get("userpassword")
        data = userdetails(userphoto=userphoto,username=username,useremail=useremail,userphone=userphone,userpassword=userpassword)
        data.save()
    return render(request,'regform.html')

def update_user_profiles(request,id):
    if request.method=="POST":
        userphoto=request.FILES["userphoto"]
        username=request.POST.get("username")
        useremail=request.POST.get("useremail")
        userphone=request.POST.get("usermobile")
        userpassword=request.POST.get("userpassword")
        data=userdetails(id=id,userphoto=userphoto,username=username,useremail=useremail,userphone=userphone,userpassword=userpassword)
        data.save()
        return redirect(user_profile)
    return render(request,'update_user_profile.html')

def update_user_profile(request,id):
    data=userdetails.objects.get(pk=id)
    return render(request,'update_user_profile.html',{'result':data})

def user_profile(request):
    u_id=request.session['uid']
    data=userdetails.objects.get(pk=u_id)
    return render(request,'user_profile.html',{'result':data})

