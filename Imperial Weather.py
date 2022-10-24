import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('API.txt', 'r').read()
Zip = input(f'Enter Zip Code you would like the current weather for:')

url = BASE_URL + f'zip={Zip},us&appid={API_KEY}&units=imperial'

while True:
    if len(Zip) > 6:
        print('Zip Code is too long - Must be 5 numbers')
        break
    elif len(Zip) < 5:
        print('Zip Code is too short - Must be 5 numbers')
        break
    else:
        break


response = requests.get(url).json()


current_temp = response['main']['temp']
feels_like = response['main']['feels_like']
condition = response['weather'][0]['main']
description = response['weather'][0]['description']

print(f'Outside in {Zip} there currently is {condition} or more specifically {description}')
print(f'The Current Temperature in {Zip} is {current_temp}F or feels like {feels_like}F')
