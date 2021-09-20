from django.shortcuts import render
import requests
from .endpoints import WEATHER_API
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

def search_weather_by_city(request):
    return render(request,'weatherapp/weather_by_city_form.html')

def show_weather_results(request):
    city_name = request.POST['city_name']
    weather = requests.get(WEATHER_API['WEATHER_BY_CITY_NAME'](city_name)).json()
    weather['dt']= datetime.fromtimestamp(weather['dt'])
    weather['sys']['sunrise'] = datetime.fromtimestamp(weather['sys']['sunrise'])
    weather['sys']['sunset'] = datetime.fromtimestamp(weather['sys']['sunset'])
    forecast = requests.get(WEATHER_API['FIVE_DAYS_FORECAST'](city_name)).json()
    context = {'weather': weather, 'forecast': forecast['list']}
    return render(request, 'weatherapp/weather_result.html',context)
    

   




    
