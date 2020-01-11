from .models import Scoreboard, Squard, Comand

def take_command_information(*args):
    if args['id']:
        print(Comand.objects.filter(id__exact = args['id']))
    return None

def register_team():
    b = Comand(name='newcommfortest')
    b.save()
    pring(b.id)
    return None
