import requests
import json

# pip install requests


api_key = '034edf104e079f9cdb84af9ffedc3c75'
ciudades = ["Moscow", "Santiago", "Buenos Aires", "Lima", "Toronto", "París", "Tokio", "Nueva York"]
#lat = 912930129
#lon = 98980


for ciudad in ciudades:

    url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
    
    respuesta = requests.get(url)

    data = respuesta.json()

    temperatura = data["main"]["temp"]
    descripcion = data["weather"][0]["description"]
    lat = data["coord"]["lat"]
    lon = data["coord"]["lon"]

    print(f"Temperatura actual en {ciudad}: {temperatura}°C")
    print(f"Descripción del clima: {descripcion}")
    print(f'Latitud  de {ciudad} es: {lat}')
    print(f'Longitud de {ciudad} es: {lon}')










