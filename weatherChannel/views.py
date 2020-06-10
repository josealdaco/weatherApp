from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Comments
from django.shortcuts import redirect

import requests

# Create your views here.

#https://community-open-weather-map.p.rapidapi.com/weather




def home(request):
    zipCode = 95110
    try:
        if request.GET['CommentBox'] is True or request.GET['CommentBox'] == 'true':
            print("This is the city", request)
            print("WE ARE SAVING A COMMENT")
            city = request.GET['city']
            comment = request.GET['Comment']
            print("This is the city", city)
            obj = Comments.objects.create(comment=comment, city=city)
            secondObject = obj
            obj.save()
            print("This is the comment being saved", secondObject.comment)
            return JsonResponse({"city": secondObject.city, "comment": secondObject.comment})
    except Exception:
        pass

    try:
        if request.GET['zipCodeBox'] is True or request.GET['zipCodeBox'] == 'true':
            zipCode = request.GET['zipCode']
            params = {
                    'access_key': 'c5b80cc09b68beb994a52dca460c3e9c',
                    'query': zipCode
                    }
            try:
                response = requests.get('http://api.weatherstack.com/current?', params)
                data = response.json()
            except Exception:
                print("Error")
                print("Error in Third Party API in User Search API")
            city = data['location']['name']
            temperature = data['current']['temperature']
            discription = data['current']['weather_descriptions'][0]
            wind = data['current']['wind_speed']
            return JsonResponse({"city": city, "temperature": temperature, "discription": discription, "wind": wind})
    except Exception:
        """ Do nothing, user has not clicked the button  yet"""
    params = {
            'access_key': 'c5b80cc09b68beb994a52dca460c3e9c',
            'query': zipCode
            }
    try:
        response = requests.get('http://api.weatherstack.com/current?', params)
        data = response.json()
    except Exception:
        print("Error")
        print("Error in Third Party API in User Search API")
    city = data['location']['name']
    temperature = data['current']['temperature']
    discription = data['current']['weather_descriptions'][0]
    wind = data['current']['wind_speed']
    commentList = Comments.objects.all()
    return render(request, 'home.html', {"city": city, "temperature": temperature, "discription": discription, "wind": wind, "comments": commentList})
