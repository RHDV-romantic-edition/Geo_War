from django.shortcuts import render
from django.http import JsonResponse
from .models import Squard, Comand, Delta
from . import APIRequests
import json
import threading
from multiprocessing import Process
import datetime, time

def reload_base():
    while(True):
        Delta.objects.all().delete()
        print('kek')
        time.sleep(1)

p = Process(target=reload_base)

def mapindex(request):
    return render(request, 'mapindex.html')

def SquaresGet():
    data = []
    bse = {}
    for e in Squard.objects.all():
        data.append(e.__str__())
        #print(e.__str__())
    for e in range(len(data)):
        a = data[e].split(':')
        bse[a[0]] = a[1]
        #print(bse[data[e]], end='\n')
    my_data = json.dumps(bse)
    return my_data

def SquareAdd(request):
    if request.method == 'POST':
        res = request.body.decode("utf-8")
        #print(res)
        res = eval(res)
        color_ = res['team']
        res = res['cords']
    coordinates = ''.join(str(res['x']) + ';' + str(res['y']))
    Sq = Squard(coord = coordinates, color = color_)
    Sq.save()
    Sq = Delta(coord = coordinates, color = color_)
    Sq.save()
    return 0

def LoginForm(request):
    return render(request, 'login.html')

def Login(request):
    Team = request.POST['team']
    password = request.POST['password']
    if password == '1111':
        return render(request, 'test.html', {'my_data': SquaresGet(), 'type': 'Suc', 'team': Team})
    return render(request, 'login.html', {'type': 'error'})

def Take_Delta(request):
    data = []
    bse = {}
    for e in Squard.objects.all():
        data.append(e.__str__())
        #print(e.__str__())
    for e in range(len(data)):
        a = data[e].split(':')
        bse[a[0]] = a[1]
        print(bse[a[0]], end='\n')
            #print(bse[data[e]], end='\n')
    return JsonResponse(bse)

#p.start()
