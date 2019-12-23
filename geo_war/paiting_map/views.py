from django.shortcuts import render
from .models import Scoreboard, Squard, Comand

def mapindex(request):
    return render(request, 'mapindex.html',)