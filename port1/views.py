from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import random

from port1.models import Facts, Info


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
    return render(request,'projects.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    about = Info.objects.get(id=1)
    return render(request,'about.html',{'info':about})