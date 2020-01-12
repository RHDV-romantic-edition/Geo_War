from django.shortcuts import render, HttpResponse
from .models import Squard, Comand
from . import APIRequests
import json

def mapindex(request):
    return render(request, 'mapindex.html')


def GetSq():
    data = []
    bse = {}
    for e in Squard.objects.all():
        data.append(e.__str__())
    for e in range(len(data)):
        a = data[e].split('.')
        data[e] = APIRequests.GetCoordinates((a[0],a[1],a[2]))
        bse[data[e]] = 'red'
    print(bse)
    return(bse)




def SquareAdd(request):
    if request.method == 'POST':
        res = request.body.decode("utf-8")
        res = eval(res)
        res = res['cords']
    coordinates = (res['lat'], res['lng'])
    Words = APIRequests.Get3Words(coordinates)
    print('Square created, word_1 = {0}, word_2 = {1}, word_3 = {2}, team = lol'.format(Words['Word_1'],Words['Word_2'],Words['Word_3']))
    Sq = Squard(word_1 = Words['Word_1'], word_2 = Words['Word_2'], word_3 = Words['Word_3'])
    Sq.save()
    data = {'word_1': Words['Word_1'], 'word_2': Words['Word_2'], 'word_3': Words['Word_3'], 'type': 'add'}
    return render(request, 'mapindex.html', data)

def SquareSearch(request):
    Word_1 = request.POST['word_1']
    Word_2 = request.POST['word_2']
    Word_3 = request.POST['word_3']
    try:
        a = Squard.objects.get(word_1 = Word_1, word_2 = Word_2, word_3 = Word_3)
    except:
        return HttpResponse('Something went wrong')
    data = {"word_1": a.word_1,"word_2": a.word_2,"word_3": a.word_3, "type": 'check'}
    return render(request, 'mapindex.html', data)

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
