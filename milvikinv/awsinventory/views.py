from django.shortcuts import render
from awsinventory.models import Servers,Rds
from django.db.models import Count
# Create your views here.

from django.http import HttpResponse

def home(request):
    ec2_region_count=Servers.objects.values('region').order_by('region').annotate(the_count=Count('region'))
    rds_region_count=Rds.objects.values('region').order_by('region').annotate(the_count=Count('region'))
    # region_count=Rds.objects.values('region').order_by('region').annotate(the_count=Count('region'))
    ec2_region_name_lst = []
    server_count_lst = []
    rds_region_name_lst = []
    rds_count_lst = []
    for records in ec2_region_count:
        ec2_region_name_lst.append(records['region'])
        server_count_lst.append(records['the_count'])
    for records in rds_region_count:
        rds_region_name_lst.append(records['region'])
        rds_count_lst.append(records['the_count'])
    
    color_list = ['#B1E278', '#BC4E55', '#5C5A72', '#D5A021', '#EEC643', '#0D21A1',
                '#E086D3', '#462749', '#00FFCD', '#4ECDC4', '#FF3333', '#4F5B69',
                '#E78F4B', '#E5E059', '#BC7D38', '#B4B241', '#6C8889',
                '#C368CA', '#E5625E', '#5F9FBF', '#BDD358']
    context = {
        'ec2_region_name_lst': ec2_region_name_lst,
        'rds_region_name_lst': rds_region_name_lst,
        'server_count_lst': server_count_lst,
        'rds_count_lst': rds_count_lst,
        'color_list': color_list
        }
    return render(request,'inventory/home-new.html',context)

def ec2(request):
    res = Servers.objects.all()
    context = {'res': res}
    return render(request,'inventory/servers.html',context)

def rds(request):
    res = Rds.objects.all()
    context = {'res': res}
    return render(request,'inventory/rds.html',context)