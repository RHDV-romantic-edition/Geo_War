from django.shortcuts import render
from .models import Scoreboard, Squard, Comand
from . import APIRequests

def mapindex(request):
    return render(request, 'mapindex.html',)

def SquareAdd(request):
    coordinates = (request.POST['latitude'], request.POST['longitude'])
    Words = APIRequests.Get3Words(coordinates)
    Team = request.POST['team']
    print('Square created, word_1 = {0}, word_2 = {1}, word_3 = {2}, team = {3}'.format(Words['Word_1'],Words['Word_2'],Words['Word_3'],Team))
    #Squard.Create(word_1 = Words['Word_1'], word_2 = Words['Word_2'], word_3 = Words['Word_3'], team = Team)
    return render(request, 'mapindex.html',)

def AlexWork(request):
    return render(request, 'test.html',)