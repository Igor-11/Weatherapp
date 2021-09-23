from django.shortcuts import render
import requests
from .endpoints import WEATHER_API
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .models import City
from django.conf import settings

def search_weather_by_city(request):
    return render(request,'weatherapp/weather_by_city_form.html')

def show_weather_results(request):
    city_name = request.POST['city_name']
    weather = requests.get(WEATHER_API['WEATHER_BY_CITY_NAME'](city_name)).json()
    weather['dt']= datetime.fromtimestamp(weather['dt'])
    weather['sys']['sunrise'] = datetime.fromtimestamp(weather['sys']['sunrise'])
    weather['sys']['sunset'] = datetime.fromtimestamp(weather['sys']['sunset'])
    forecast = requests.get(WEATHER_API['FIVE_DAYS_FORECAST'](city_name)).json()
    cities = City.objects.exclude(longitude=weather['coord']['lon'],latitude=weather['coord']['lat']) 
    if not City.objects.filter(latitude=weather['coord']['lat'], longitude=weather['coord']['lon']).exists():
        city = City(name=city_name, latitude=weather['coord']['lat'], longitude=weather['coord']['lon'])
        city.save()
    context = {'weather': weather, 'forecast': forecast['list'], 'map_api_key' : settings.MAP_API_KEY, 'cities': cities}
    return render(request, 'weatherapp/weather_result.html',context)

def show_history(request):
    cities = City.objects.all()
    context = {'cities' : cities}
    return render(request, 'weatherapp/history.html',context)

def delete_history(request):
    City.objects.all().delete()
    return HttpResponseRedirect(reverse('search_weather'))

def delete_city(request, pk):
    City.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('show_history'))

    

   




    
