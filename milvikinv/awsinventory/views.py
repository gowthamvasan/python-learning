from django.shortcuts import render
from awsinventory.models import servers,db
# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request,'inventory/home.html')

def ec2(request):
    res = servers.objects.all()
    context = {'res': res}
    return render(request,'inventory/servers.html',context)

def rds(request):
    res = db.objects.all()
    context = {'res': res}
    return render(request,'inventory/rds.html',context)