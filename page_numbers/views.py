from django.shortcuts import render, redirect, HttpResponse
from django.apps import apps
User = apps.get_model('login', 'User')
from .models import *

def index(request):
    all_leads = Lead.objects.all()[:5]
    context = {
        'all_leads':all_leads,
        'id':1,
    }
    return render(request,'pages/index.html', context)

def next_table(request, id):
    new_item = Lead.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], from_date=request.POST['from_date'], to_date=request.POST['to_date'])

    all_leads = Lead.objects.all()[(id*5)-5:id*5]

    context = {
        'all_leads':all_leads,
        'new_item':new_item,
        'id':id,
    }
    return render(request, 'pages/table.html', context)

def change_page(request, id):
    all_leads = Lead.objects.all()[(id*5)-5:id*5]

    context={
        'all_leads': all_leads,
        'id':id,
    }
    return render(request, 'pages/table.html', context)

# Create your views here.
