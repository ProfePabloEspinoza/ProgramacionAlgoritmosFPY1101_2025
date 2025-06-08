"""
Pide al usuario que escriba el nombre de una ciudad. Consulta la API y muestra la temperatura y una sugerencia.
Repite esto hasta que el usuario escriba "salir".

"""

import requests

api_key = "034edf104e079f9cdb84af9ffedc3c75"

while True:
    ciudad = input("Escribe una ciudad para consultar el clima (o 'salir' para terminar): ")
    if ciudad.lower() == "salir":
        print("¡Hasta luego!")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        data = respuesta.json()
        temperatura = data["main"]["temp"]
        descripcion = data["weather"][0]["description"]

        print(f"{ciudad.title()}: {temperatura}°C - {descripcion}")
        
        if temperatura < 10:
            print("Recomendación: Hace frío, lleva abrigo.")
        elif temperatura > 25:
            print("Recomendación: Hace calor, ropa ligera.")
        else:
            print("Recomendación: Clima templado.")
    else:
        print("Ciudad no encontrada. Intenta nuevamente.")
