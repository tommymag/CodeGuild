import requests
city = input("enter the city where you would like to know the weather: ")
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=343eeef0fd916aa63ef640f9fd3cb421"
data = rt.get(url)
read = data.json()
print("Cityname : {} ".format(read['name']))
print("Temperature : {} ".format(read['main']['temp']))
print("Humidity : {}".format(read['main']['humidity']))
print("pressure : {} ".format(read['main']['pressure']))
print("Wind Speed : {} ".format(read['wind']['speed']))
print("details : {} ".format(read['weather'][0]['description']))
ask=raw_input("Do you want to know another city info(y/n)?")
if ask=="y":
    var = True
else:
    var = False﻿