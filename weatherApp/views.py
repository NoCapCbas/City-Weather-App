from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import WeatherForm
from django.http import JsonResponse

# Create your views here.
def main(request):
    context = {}
    city='New York'
    input_error=False
    error_statement = 'Please input a valid City Name'
    form = WeatherForm()
    context['form'] = form

    cities = City.objects.all()

    return render(request, 'weatherApp/index.html', context)

def getWeather(request):
    json_response_obj = {
        'success' : False,
        'data' : None,
        'errors': None,
    }
    #Open Weather Api
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=21d3fc8fd581dd07957096f087ab574c'

    app_post_request_data = request.GET
    if 'location' in app_post_request_data:
        location = app_post_request_data['location']
    else: 
        location = None

    form = WeatherForm(app_post_request_data)
    if request.method == 'GET':
        if form.is_valid():
            form.save()

            weather_api_response = requests.get(url.format(location))
            weather_data_json = weather_api_response.json()
            # print(weather_data_json)
            if weather_data_json['cod'] == '404':
                
                json_response_obj['success'] = False
                json_response_obj['data'] = weather_data_json
                status_code = 404
            else:

                json_response_obj['success'] = True
                json_response_obj['data'] = weather_data_json
                status_code = 200
        else:
            errors = {}
            for field, error_messages in form.errors.items():
                errors[field] = list(error_messages)

            json_response_obj['success'] = False
            json_response_obj['errors'] = errors
            status_code = 400

    
    return JsonResponse(json_response_obj, status=status_code)

