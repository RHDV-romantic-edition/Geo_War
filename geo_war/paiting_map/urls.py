from django.urls import path
from . import views, functions


urlpatterns = [
    path('', views.mapindex, name='map'),
    path('Alex/', views.AlexWork, name='alex'),
    path('square_add/', views.SquareAdd, name='square_add'),
    path('square_check/', views.SquareSearch, name='square_check')
]
