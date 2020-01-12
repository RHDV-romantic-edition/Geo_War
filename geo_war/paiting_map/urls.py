from django.urls import path
from . import views, functions


urlpatterns = [
    path('testmap', views.mapindex, name='test'),
    path('', views.AlexWork, name='work'),
    path('square_add/', views.SquareAdd, name='square_add'),
    path('square_check/', views.SquareSearch, name='square_check'),
]