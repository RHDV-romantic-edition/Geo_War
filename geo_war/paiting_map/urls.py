from django.urls import path
from . import views, functions


urlpatterns = [
    path('testmap', views.mapindex, name='test'),
    path('', views.LoginForm, name='work'),
    path('login/', views.Login, name='work'),
    path('square_add/', views.SquareAdd, name='square_add'),
    path('square_add/', views.SquareAdd, name='square_add'),
    path('get_delta/', views.Take_Delta, name='TakeDelta'),
]
