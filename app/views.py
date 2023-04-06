from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_Topic(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('data inserted into topic table')

def insert_Webpage(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter name : ')
    u=input('enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('data inserted into Webpage')

def insert_Accessrecord(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter name : ')
    u=input('enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    
    WO.save()
    a=input('Enter Author name : ')
    d=input('Enter date : ')
    AO=Accessrecord.objects.get_or_create(name=WO,author=a,date=d)[0]
 
    AO.save()
    return HttpResponse('Data inserted into Accessrecord')   



