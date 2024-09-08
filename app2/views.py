from django.shortcuts import render,redirect
from pro1.models import details
from ADMIN.models import doctorlist
from . models import *
# Create your views here.
def userprofile(request):
    u_id=request.session['uid']
    data=details.objects.get(pk=u_id)
    return render(request,'userprofile.html',{'result':data})

def bookappointment(request):
    details=doctorlist.objects.all()
    if request.method=="POST":
        patient_name=request.POST.get("patient_name")
        patient_email=request.POST.get("patient_email")
        patient_mobile=request.POST.get("patient_mobile")
        patient_doctor=request.POST.get("patient_doctor")
        patient_date=request.POST.get("patient_date")
        patient_problem=request.POST.get("patient_problem")
        book_app=appointments(patient_name=patient_name,patient_email=patient_email,patient_mobile=patient_mobile,patient_doctor=patient_doctor, patient_date= patient_date,patient_problem=patient_problem)
        book_app.save()
        return redirect(bookappointment)
    return render(request,'user_appointment.html'),{{'result':details}}
        


     
    