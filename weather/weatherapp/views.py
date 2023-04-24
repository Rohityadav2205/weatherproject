import json

import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse("App Home")


def weather(request):
    city = "Varanasi"
    if request.GET:
        print("get")
        city = request.GET["city"]
        path = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=8ffe2740aa37259e39e855b706122009&units=metric"
        response = requests.get(path)
        print(response.text)
        code = response.status_code
        if code != 200:
            print("Not found")
        else:
            print(response.status_code)
            jsondata = json.loads(response.text)
            wmain = jsondata["weather"][0]['main']
            currenticon = jsondata["weather"][0]['icon']
            wdescription = jsondata["weather"][0]['description']
            temp = jsondata.get("main").get("temp")
            print(temp, "deg Celsius")
            temp_min=jsondata.get("main").get("temp")
            print(temp_min,"deg celsious")
            temp_max=jsondata.get("main").get("temp")
            print(temp_max,"deg celsious")
            pressure=jsondata.get("main").get("pressure")
            print(pressure," ")
            humidity=jsondata.get("main").get("humidity")
            print(humidity," ")
            visibility=jsondata.get("main").get("visibility")
            print(visibility," ")
        return render(request, "show data.html",
                      {"weather": response.text, "code": wmain, "city": city, "currenticon": currenticon, "wdescription":wdescription, "temp":temp})
    return render(request, "show data.html", {"weather": "", "code": "", ",city": ""})



