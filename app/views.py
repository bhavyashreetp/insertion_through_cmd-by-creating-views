from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    tn=input('enter topicname')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is inserted')


def insert_webpage(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('webpage is created')



def insert_accessrecord(request):
    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name')
    u=input('enter url')
    d=(input('enter date'))
    a=input('enter author')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse('accessrecord is inserted')




