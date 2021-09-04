# DSC 510
# week 12
# Programming Final Assignment Week 12
# Created a weather application that interacts with a webservice to obtain weather data to display for the user.
# Which prompts the user for the city or zip code and request weather forecast data from OpenWeatherMap.
# Author Theodore Koby-Hercsky
# 06/03/2021


# Change Control Log:
# Change#:1
# Change(s) Made:
# Author: Theodore Koby-Hercsky
# Change Approved by: Theodore Koby-Hercsky
# Date Moved to Production: 06/04/2021

import time
import requests
import json

# Displayed a welcome message for the user
print("Welcome to the weather program, where you can get the latest weather report in an instant.")


# The main function requests a user to enter a city or zip code to get the latest weather report.


def main():
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    city_or_zip = input('What city, country or zip code are you requesting: ')
    while True:
        try:
            weather(city_or_zip, weather_url)
            print('----------------------------------------------')
            another_one()
            break
        except LookupError:
            print('----------------------------------------------')
            another_one()
            break


# Created the weather function that uses a get request for the weather url that receives the weather
# While connecting and displaying the weather information


def weather(city_or_zip, weather_url):
    if city_or_zip.isdigit() is True:
        param = {'zip': city_or_zip, 'APPID': '481c487c9b2b7634971be29cdd8a8516'}
    else:
        param = {'q': city_or_zip, 'APPID': '481c487c9b2b7634971be29cdd8a8516'}
    answer = requests.get(weather_url, params=param, timeout=(5, 14))
    weather_site(answer, city_or_zip)
    if answer.status_code == 200:
        print('connection made')
    parsed = json.loads(answer.text)
    display_weather(parsed)


# The temperature function converts the temperature from kelvin to fahr and cel.


def temperature(degree):
    celsius = round(degree - 273.15)
    fahrenheit = round((((degree - 273.15)*9)/5)+32)
    return f'{fahrenheit}{chr(176)}F / {celsius}{chr(176)}C'


# The weather site function creates a except block which makes sure the request works.
# while also validating if the city and or zip code is correct


def weather_site(answer, city_or_zip):
    try:
        answer.raise_for_status()
    except requests.HTTPError as incorrect:
        if answer.status_code == 404:
            if city_or_zip.isdigit() is True:
                print(f"Zip code '{city_or_zip}' is incorrect.")
            else:
                if city_or_zip.__contains__(','):
                    print(f"Invalid city'{city_or_zip[0:-2].title() + city_or_zip[-2:].upper()}'")
                else:
                    print(f"Unavailable city'{city_or_zip.title()}'")
        else:
            print('Invalid zip code please try a different location')
            print(f'{incorrect}')


# The display weather function formats the Json data to make it ledgible for the user.


def display_weather(formats):
    timezone = int(json.dumps(formats['timezone']))
    times = int(json.dumps(formats['dt']))
    actual_time = times + timezone
    present_time = time.strftime("%A, %b %d, %Y %I:%M %p (local time)", time.gmtime(actual_time))
    city = str(json.dumps(formats['name'])).replace('"', '')
    country = str(json.dumps(formats['sys']['country'])).replace('"', '')
    temperatures_min = float(json.dumps(formats['main']['temp_min']))
    temperatures_max = float(json.dumps(formats['main']['temp_max']))
    temperatures = float(json.dumps(formats['main']['temp']))
    description = str(json.dumps(formats['weather'][0]['description'])).replace('"', '').title()
    print(f'{city}, {country} Current weather on {present_time}')
    print(f'{temperature(temperatures)} is the temperature.')
    print(f'{temperature(temperatures_min)}')
    print(f'{temperature(temperatures_max)}')
    print(f'please expect {description} throughout the day\n')


# The another one function asks the user if they would like to see another weather forecast or finish
# By using a while loop and determining if they said yes or no to either return to the main function or exit.


def another_one():
    question = str(input(f'Do you want to view the weather for another location?\n'
                         f'Please signify by entering yes or no: ')).lower().strip()
    while not (question == 'yes' or question == 'no'):
        question = str(input('Incorrect input please type yes or no to proceed: ')).lower().strip()
    if question == 'yes':
        print('----------------------------------------------')
        main()
    if question == 'no':
        print('Thanks for stopping by and have a great day!')


main()
