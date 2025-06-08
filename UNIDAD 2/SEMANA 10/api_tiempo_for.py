"""

Crea una lista con 5 ciudades diferentes. Usa un ciclo for para recorrer cada ciudad y consultar su temperatura actual usando la API de OpenWeatherMap.

Para cada ciudad:
- Si la temperatura es menor a 10°C, imprimir: "Frío en [ciudad], abrígate bien."
- Si está entre 10°C y 25°C, imprimir: "Clima agradable en [ciudad]."
- Si es mayor a 25°C, imprimir: "Hace calor en [ciudad], lleva ropa ligera."

ciudades = ["Santiago", "Buenos Aires", "Lima", "Madrid", "Toronto", "París", "Nueva York", "Tokio", "Moscow"]

"""
import requests
import json

api_key = "034edf104e079f9cdb84af9ffedc3c75"
ciudades = ["Santiago", "Buenos Aires", "Lima", "Madrid", "Toronto", "París", "Nueva York", "Tokio", "Moscow"]


for ciudad in ciudades:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    data = respuesta.json()
    
    temperatura = data["main"]["temp"]
    descripcion = data["weather"][0]["description"]
    
    if temperatura < 10:
        print(f"Frío en {ciudad}, abrígate bien.")
        print(f'temperatura: {temperatura}')
        print(f"clima: {descripcion}.")
        
    elif temperatura <= 25:
        print(f"Clima agradable en {ciudad}.")
        print(f'temperatura: {temperatura}')
        print(f"clima: {descripcion}.")
               
    else:
        print(f"Hace calor en {ciudad}, lleva ropa ligera.")
        print(f'temperatura: {temperatura}')
        print(f"clima: {descripcion}.")

# Imprimir con formato legible
print(json.dumps(data, indent=4, ensure_ascii=False))
        


