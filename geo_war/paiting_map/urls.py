from django.urls import path
from . import views, functions


urlpatterns = [
    path('', views.mapindex, name='map'),
    path('getCommand/<int:id>/', functions.take_command_information, name='get_codmand'),
    path('make/<int:name>/', functions.register_team, name='makecommand'),
]