from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search_weather_by_city, name='search_weather'),
    path('results', views.show_weather_results, name='weather_results')
]