from django.shortcuts import render, HttpResponse
from .models import Scoreboard, Squard, Comand
from . import APIRequests

def mapindex(request):
    return render(request, 'mapindex.html',)

def SquareAdd(request):
    coordinates = (request.POST['latitude'], request.POST['longitude'])
    Words = APIRequests.Get3Words(coordinates)
    Team = request.POST['team']
    print('Square created, word_1 = {0}, word_2 = {1}, word_3 = {2}, team = {3}'.format(Words['Word_1'],Words['Word_2'],Words['Word_3'],Team))
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
