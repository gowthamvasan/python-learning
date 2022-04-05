from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ec2/', views.ec2, name='ec2'),
    path('rds/', views.rds, name='rds'),
]