from django.conf import settings

WEATHER_API = {
    'WEATHER_BY_CITY_NAME': lambda city_name:f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={settings.WEATHER_API_KEY}',
    'FIVE_DAYS_FORECAST': lambda city_name:f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={settings.WEATHER_API_KEY}'
}