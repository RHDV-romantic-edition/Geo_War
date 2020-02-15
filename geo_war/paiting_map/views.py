#import django libraries 
from django.shortcuts import render
from django.http import JsonResponse
#import DataBases from .models
from .models import Squard, Comand, Delta
#import Process to start functions parallel
from multiprocessing import Process
#import datretime and time to clear Delta Tables
import datetime, time, json
#import variables from Config file
from .CONFIG import WIGTH, HEIGHT
w = WIGTH
h = HEIGHT

#the functoin that cleans DeltaBase
def reload_base():
    while(True):
        Delta.objects.all().delete()
        print('kek')
        time.sleep(1)

def mapindex(request):
    return render(request, 'main.html')

def SquaresGet():
    data = []
    bse = {}
    for e in Squard.objects.all():
        data.append(e.__str__())
        #print(e.__str__())
    for e in range(len(data)):
        a = data[e].split(':')
        coordinates = a[0].split(';')
        coordinates = '{0};{1};{2};{3}'.format(float(coordinates[1]), float(coordinates[1]) + h,float(coordinates[0]) + w, float(coordinates[0]))
        bse[coordinates] = a[1]
    my_data = json.dumps(bse)
    return my_data

def SquareAdd(request):
    if request.method == 'POST':
        res = request.body.decode("utf-8")
        res = eval(res)
        print('______________________________-')
        print(res)
        print('______________________________-')
        color_ = res['team']
        print('Color is: ', color_)
        res = res['cords']
        print('Cords is: ', res)

    res[0] = (res[0]//w)*w
    res[1] = (res[1]//h)*h

    coordinates = ''.join(str(res[0]) + ';' + str(res[1]))
    Sq = Squard(coord = coordinates, color = color_)
    Sq.save()
    #Sq = Delta(coords = coordinates, color = color_)
    #Sq.save()
    print('FLEEXXXXXX')
    return JsonResponse({0:0})

def LoginForm(request):
    return render(request, 'login.html')

def Login(request):
    col = {
    'blue': '#0000FF',
    'green': '#00FF00',
    'red': '#FF0000',
    'white': '#FFFFFF',

    }
    Team = request.POST['team']
    password = request.POST['password']
    if password == '1111':
        print('-----------COLOR-----------')
        print(col[Team])
        print('-----------------------')
        return render(request, 'main.html', {'my_data': SquaresGet(), 'type': 'Suc', 'team': col[Team]})
    return render(request, 'login.html', {'type': 'error'})

def Take_Delta(request):
    data = []
    bse = {}
    for e in Delta.objects.all():
        data.append(e.__str__())
    for e in range(len(data)):
        a = data[e].split(':')
        coordinates = a[0].split(';')
        coordinates = '{0};{1};{2};{3}'.format(float(coordinates[1]) + h, float(coordinates[1]),float(coordinates[0]) + w, float(coordinates[0]))
        bse[coordinates] = a[1]
    return JsonResponse(bse)

#Start MultiProcessing
p = Process(target=reload_base)
p.start()
