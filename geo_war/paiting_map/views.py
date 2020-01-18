from django.shortcuts import render, HttpResponse
from .models import Squard, Comand
from . import APIRequests
import json

def mapindex(request):
    return render(request, 'mapindex.html')

def SquaresGet():
    data = []
    bse = {}
    for e in Squard.objects.all():
        data.append(e.__str__())
    for e in range(len(data)):
        a = data[e].split('.')
        print(a)
        data[e] = APIRequests.GetCoordinates((a[0],a[1],a[2]))
        bse[data[e]] = "#FF0000"
    my_data = json.dumps(bse)
    return my_data

def SquareAdd(request):
    if request.method == 'POST':
        res = request.body.decode("utf-8")
        res = eval(res)
        color_ = 'red'#res['color']
        res = res['cords']
    coordinates = (res['lat'], res['lng'])
    Words = APIRequests.Get3Words(coordinates)
    print('Square created, word_1 = {0}, word_2 = {1}, word_3 = {2}, team = lol'.format(Words['Word_1'],Words['Word_2'],Words['Word_3']))
    Sq = Squard(word_1 = Words['Word_1'], word_2 = Words['Word_2'], word_3 = Words['Word_3'], color = color_)
    Sq.save()
    data = {'word_1': Words['Word_1'], 'word_2': Words['Word_2'], 'word_3': Words['Word_3'], 'type': 'add'}
    return render(request, 'mapindex.html', data)

def LoginForm(request):
    return render(request, 'login.html')

def Login(request):
    Team = request.POST['team']
    password = request.POST['password']
    if password == '1111':
        return render(request, 'test.html', {'my_data': SquaresGet(), 'type': 'Suc'})
    return render(request, 'login.html', {'type': 'error'})

def AlexWork(request):
    data = []
    bse = {}
    for e in Squard.objects.all():
        data.append(e.__str__())
    for e in range(len(data)):
        a = data[e].split('.')
        print(a)
        data[e] = APIRequests.GetCoordinates((a[0],a[1],a[2]))
        bse[data[e]] = 'red'
    my_data = json.dumps(bse)
    print(my_data)
    return render(request, 'test.html', {'my_data': my_data})
