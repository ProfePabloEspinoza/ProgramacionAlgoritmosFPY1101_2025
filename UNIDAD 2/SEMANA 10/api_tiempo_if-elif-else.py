import requests

api_key = "034edf104e079f9cdb84af9ffedc3c75"
ciudad = "Santiago"
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

respuesta = requests.get(url)
data = respuesta.json()

print(data)

# # Presiona Shift + Alt + F (en Windows) o Shift + Option + F (en macOS).

temperatura = data["main"]["temp"]
descripcion = data["weather"][0]["description"]

print(f"Temperatura actual en {ciudad}: {temperatura}°C")
print(f"Descripción del clima: {descripcion}")

if "lluvia" in descripcion.lower() or "rain" in descripcion.lower():
    print("Parece que lloverá, lleva un paraguas.")
elif temperatura < 15:
    print("Hace frío, sal con chaqueta.")
elif temperatura > 25:
    print("Hace calor, puedes salir con ropa ligera.")
else:
    print("El clima está agradable, sal como te sientas cómodo.")
