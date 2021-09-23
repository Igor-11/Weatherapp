from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search_weather_by_city, name='search_weather'),
    path('results', views.show_weather_results, name='weather_results'),
    path('history', views.show_history, name='show_history'),
    path('delete-histoty', views.delete_history, name='delete_history'),
    path('delete-city/<int:pk>', views.delete_city, name='delete_city'),
]