from django.shortcuts import render, redirect
from .models import city
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


# Create your views here.
def home(request):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2d3728bbf0c026185a259b0c835b7d7'

    current_city_weather = []
    for city_loc in city.objects.all():
        json = requests.get(api_url.format(city_loc)).json()

        weather = {
            'city': city_loc,
            'temprature': round(json['main']['temp']-273.15),
            'description': json['weather'][0]['description'],
            'icon': json['weather'][0]['icon']
        }

        current_city_weather.append(weather)


    if request.method == "POST":
        city_loc = request.POST.get('city')
        json = requests.get(api_url.format(city_loc)).json()

        
        if json['cod'] == 200:
            try :
                go = city.objects.get(city_name=city_loc)
                return redirect('/')
            except ObjectDoesNotExist:
                citys = city()
                citys.city_name = city_loc
                citys.save()
                return redirect('/')
    
        else:
            return HttpResponse("Please Enter valid city/country!")

        
    return render(request, 'home.html', {'citys': city.objects.all(), 'weathers':current_city_weather})