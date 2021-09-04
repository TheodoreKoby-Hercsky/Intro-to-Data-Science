import requests
import json
import time

print("Welcome to the weather program, where you can get the latest weather report in an instant.")


def main():
    """Main function for the program, allows user to input a zip code or city to receive current/future forecast"""
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    city_or_zip = input('What city, country or zip code are you requesting: ')
    while True:
        try:
            weather(city_or_zip, weather_url)
            print('')
            another_one()
            break
        except LookupError:
            print('')
            another_one()
            break


def weather(city_or_zip, weather_url):
    """Makes a GET request to the url for current weather, verifies connection is made, parses and displays the data"""
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


def convert_temp(degree):
    """Converts Kelvin temperatures to Fahrenheit and Celsius"""
    celsius = round(degree - 273.15)
    fahrenheit = round((((degree - 273.15) * 9) / 5) + 32)
    return f'{fahrenheit}{chr(176)}F / {celsius}{chr(176)}C'


def weather_site(answer, city_or_zip):
    """Try Except block to test the request was successful, additionally checking if the city or
    zip code entered is valid by using 404 status code"""
    try:
        answer.raise_for_status()
    except requests.HTTPError as error:
        if answer.status_code == 404:
            if city_or_zip.isdigit() is True:
                print(f"Zip code '{city_or_zip}' is incorrect.")
            else:
                if city_or_zip.__contains__(','):
                    print(f"Invalid city '{city_or_zip[0:-2].title() + city_or_zip[-2:].upper()}'")
                else:
                    print(f"Unavailable city '{city_or_zip.title()}'")
        else:
            print('Invalid zip code please try a different location')
            print(f'{error}')

def display_weather(formats):
    """Decodes the JSON data, formats the time variables to match proper time zones, then formats the printable
    output of the current weather"""
    city = str(json.dumps(formats['name'])).replace('"', '')
    country = str(json.dumps(formats['sys']['country'])).replace('"', '')
    timezone = int(json.dumps(formats['timezone']))
    times = int(json.dumps(formats['dt']))
    actual_time = times + timezone
    present_time = time.strftime("%A, %b %d, %Y %I:%M %p (local time)", time.gmtime(actual_time))
    temperatures = float(json.dumps(formats['main']['temp']))
    conditions = str(json.dumps(formats['weather'][0]['description'])).replace('"', '').title()
    print(f'Weather Report for {city}, {country} on {present_time}:\n'
          f'Current Temperature {convert_temp(temperatures)}\n'
          f'Current Conditions: {conditions}\n')


def another_one():
    """Allows the user to look up another location or exit the program"""
    option = str(input('Would you like to enter another location, Yes or No? ')).lower().strip()
    # while loop for a yes selection or to exit the program (and to catch input errors)
    while not (option == 'yes' or option == 'no'):
        option = str(input('You did not enter a valid selection.\n'
                           'Please enter Yes to search another location or No to exit: ')).lower().strip()
    if option == 'yes':
        print('')
        main()
    if option == 'no':
        print('Thank you for using our service. Goodbye')


main()
