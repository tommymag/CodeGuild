# Lab: PyWeather

# Create a program that will prompt a user for city name or zip code. Use that information to get the current weather.
# Display that information to the user in a clean way.

import requests                                                 # asking python to open the package
question = input('Would you like to search by (c)ity name or (z)ip?: ')  # User input statement which later is assigned during a conditional
city = input("What city or zip are you looking for?: ")         # assigns neatly for the user when the program already is assigned which way they will search
package = {
    'APPID': "343eeef0fd916aa63ef640f9fd3cb421",                  # package and my specific ID assigned by the website
}
if question == 'c':                                              # literally c will be the only input that returns relevant info with a city name
    package['q'] = city                                         # this triggers paramaters which will be accessing the data
else:
    package['zip'] = city                   # anything else written into the input will prepare the program to get five numbers to access the data

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)     # This is where the data will be coming from and relating back to the package

data = r.json()                             # a constructor to look into json dat(dictionary form in python)
print("The current temperature is: {} degrees F".format(round(int(data['main']['temp'])* (9/5) - 459.67))) # Changes the string to an integer and rounds the farenhight for the user
print("Humidity : {}".format(data['main']['humidity']))     # prints humidity key
print("Wind Speed : {} m/s".format(data['wind']['speed']))  # prints wind speed with the descriptor
print("What it's like out there : {} ".format(data['weather'][0]['description']))  # prints what it's like