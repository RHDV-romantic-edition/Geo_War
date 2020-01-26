from django.shortcuts import render
from django.http import JsonResponse
from .models import Squard, Comand, Delta
from . import APIRequests
import json
import threading
from multiprocessing import Process, Pool
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
        ab = a[0].split('.')
        data[e] = APIRequests.GetCoordinates((ab[0],ab[1],ab[2]))
        bse[data[e]] = a[1]
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
    coordinates = (res['lat'], res['lng'])
    Words = APIRequests.Get3Words(coordinates)
    #print('Square created, word_1 = {0}, word_2 = {1}, word_3 = {2}, team = lol'.format(Words['Word_1'],Words['Word_2'],Words['Word_3']))
    Sq = Squard(word_1 = Words['Word_1'], word_2 = Words['Word_2'], word_3 = Words['Word_3'], color = color_)
    Sq.save()
    Sq = Delta(coords = ''.join(Words['Word_1'] +'.' + Words['Word_2'] + '.' + Words['Word_3']), color = color_)
    Sq.save()
    data = {'word_1': Words['Word_1'], 'word_2': Words['Word_2'], 'word_3': Words['Word_3'], 'type': 'add'}
    return render(request, 'mapindex.html', data)

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
    if request.method == 'GET':
        for e in Delta.objects.all():
            data.append(e.__str__())
            #print(e.__str__())
        for e in range(len(data)):
            a = data[e].split(':')
            ab = a[0].split('.')
            #print(ab[0],ab[1],ab[2], sep=' ')
            ac = a[1]
            data[e] = APIRequests.GetCoordinates((ab[0],ab[1],ab[2]))
            bse[data[e]] = a[1]
            #print(bse[data[e]], end='\n')
    return JsonResponse(bse)

p.start() 