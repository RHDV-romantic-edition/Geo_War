from django.shortcuts import render
from django.http import JsonResponse
from .models import Squard, Comand, Delta
from . import APIRequests
import json
import threading
from multiprocessing import Process
import datetime, time

w = 0.0006
h = 0.0006

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
        coordinates = a[0].split(';')
        coordinates = '{0};{1};{2};{3}'.format(float(coordinates[1]), float(coordinates[1]) - h,float(coordinates[0]), float(coordinates[0]) + w)
        bse[coordinates] = a[1]
    my_data = json.dumps(bse)
    return my_data

def SquareAdd(request):
    if request.method == 'POST':
        res = request.body.decode("utf-8")
        #print(res)
        res = eval(res)
        color_ = res['team']
        res = res['cords']
    
    res['lat'] = (res['lat']//w)*w
    res['lng'] = (res['lng']//h)*h

    coordinates = ''.join(str(res['lat']) + ';' + str(res['lng']))
    Sq = Squard(coord = coordinates, color = color_)
    Sq.save()
    Sq = Delta(coords = coordinates, color = color_)
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
    for e in Delta.objects.all():
        data.append(e.__str__())
    for e in range(len(data)):
        a = data[e].split(':')
        coordinates = a[0].split(';')
        coordinates = '{0};{1};{2};{3}'.format(float(coordinates[1]), float(coordinates[1]) - h,float(coordinates[0]), float(coordinates[0]) + w)
        bse[coordinates] = a[1]
        print(bse[coordinates], end='\n')
    return JsonResponse(bse)

#p.start()
