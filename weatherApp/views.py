from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    #Open Weather Api
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=21d3fc8fd581dd07957096f087ab574c'

    city='New York'
    input_error=False
    error_statement = 'Please input a valid City Name'




    if request.method == 'POST':
        var = request.POST
        city = var['name']
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()


    form = CityForm()


    cities = City.objects.all()




    #uses open weather api
    r = requests.get(url.format(city)).json()



    #Input Error Check: executes if city name is not recognized
    if r['cod'] == '404':
        input_error=True

        r = requests.get(url.format('New York')).json()
        city_weather = {
            'city': r['name'],
            'temp': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        str = city_weather.get('icon')
        str = str[:-1]
        imgPath = getImg(str)

        context = {'city_weather': city_weather, 'form':form, 'imgPath': imgPath, 'input_error':input_error,
            'error_statement': error_statement}
        return render(request, 'weatherApp/index.html', context)

    #End Error Check: ignores error check if city is recognized


    city_weather = {
        'city': r['name'],
        'temp': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    #assigns background image
    str = city_weather.get('icon')
    str = str[:-1]
    imgPath = getImg(str)




    context = {'city_weather': city_weather, 'form':form, 'imgPath': imgPath, 'input_error':input_error,
        'error_statement': error_statement}
    return render(request, 'weatherApp/index.html', context)

# Gets the background image using api icon code and returns it to be used in the index
def getImg(str):

        if str == '04':

            imgPath = 'images/broken_clouds.jpg'
            return imgPath
        elif str == '01':

            imgPath = 'images/clear_sky.jpg'
            return imgPath

        elif str == '02':

            imgPath = 'images/few_clouds.jpg'
            return imgPath
        elif str == '03':

            imgPath = 'images/scattered_clouds.jpg'
            return imgPath
        elif str == '09':

            imgPath = 'images/shower_rain.jpg'
            return imgPath
        elif str == '10':

            imgPath = 'images/rain.jpg'
            return imgPath
        elif str == '11':

            imgPath = 'images/thunderstorm.jpg'
            return imgPath
        elif str == '13':

            imgPath = 'images/snow.jpg'
            return imgPath
        elif str == '50':

            imgPath = 'images/mist.jpg'
            return imgPath
        else:
            imgPath = 'images/default.jpg'
            return imgPath
