from .models import Squard, Comand

def take_command_information(*args):
    if args['id']:
        print(Comand.objects.filter(name__exact = 'Green'))
    return None

def register_team():
    b = Comand(name='newcommfortest')
    b.save()
    pring(b.id)
    return None
