from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('getWeather/', views.getWeather, name='getWeather'),
]
