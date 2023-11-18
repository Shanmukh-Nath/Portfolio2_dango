from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt
import random

from port1.models import Facts, Info, Projects


@xframe_options_exempt
def index(request):
    facts = Facts.objects.all()
    n = len(facts) - 1
    rand_fact_n = random.randint(0,n)
    rand_fact = facts[rand_fact_n]
    return render(request,'index.html',{'fact':rand_fact})
# Create your views here.

def bedroom_spline(request):
    return render(request,'bedroom_spline.html')

def about_spline(request):
    return render(request,'about_spline.html')

def projects(request):
    projects = Projects.objects.all()
    return render(request,'projects.html',{'projects':projects})

def contact(request):
    if request.method=='POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        reason = request.POST.get('reason')
        rec_email = 'shanmukh733@gmail.com'
        subject = f'{name} has Contacted You.'
        msg = f'{name} has Contacted You with a purpose\nReason : {reason} \nYou can contact him through\nContact :{email}'
        try:
            send_mail(subject,msg,'noreply@exam.in',[rec_email])
            messages.success(request,'Email Sent Successfully')
            return redirect('home')
        except Exception:
            messages.error(request,"Couldn't Send Email, Please try again")
            return redirect('contact')

    return render(request,'contact.html')

def about(request):
    about = Info.objects.get(id=1)
    return render(request,'about.html',{'info':about})