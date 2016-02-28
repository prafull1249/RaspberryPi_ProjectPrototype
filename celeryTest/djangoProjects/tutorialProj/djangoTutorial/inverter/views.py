from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.utils import timezone
from django.core.context_processors import csrf
from models import inverterAsu

#def index(request):
#    return HttpResponse("Hello, This is inverter application")

#def getRequest(request):
def index(request):
    #health = request.GET['health']
    #a = open('file','r+')
    #print(health)
    health = request.GET['health']
    temp = request.GET['temp']
    prod = request.GET['prod']
    switch = request.GET['switch']
    uptime = request.GET['uptime']
    idx = request.GET['id']
    if switch=="OFF":
       switchl= 0
    else:
       switchl = 1
    #q = inverterAsu(prod=prod, temp = temp ,health=health, activeSince=timezone.now(),vendor="Frolicki",uptime=uptime, switch= switchl)
    q = inverterAsu.objects.get(id=idx)
    q.health = health
    q.temp = temp
    q.uptime = uptime
    q.switch = switch
    q.save()
    return HttpResponse(switch)

