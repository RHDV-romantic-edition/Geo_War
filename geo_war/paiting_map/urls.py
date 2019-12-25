from django.urls import path
from . import views


urlpatterns = [
    path('', views.mapindex, name='map'),
    path('square_add/', views.SquareAdd, name='square_add')
]
