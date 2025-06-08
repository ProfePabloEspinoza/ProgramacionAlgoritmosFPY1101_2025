# Este es un programa de ejemplo en Python
# Variables y Tipos de Datos
# Para ejecutar una parte de este programa, deberás comentar las secciones que no probarás
variable_entera = 42  # Entero
variable_decimal = 3.14  # Decimal
variable_texto = "Hola, mundo!"  # Cadena de texto
variable_booleana = True  # Valor booleano

# Operadores
resultado_suma = variable_entera + variable_decimal
comparacion = (variable_entera > variable_decimal)

# Estructuras de Control de Flujo
if variable_booleana:
    print("La variable booleana es verdadera.")
elif resultado_suma < 10:
    print("La suma es menor que 10.")
else:
    print("Ninguna de las condiciones anteriores se cumple.")

# Colecciones de Datos
lista_numeros = [1, 2, 3, 4, 5]
tupla_colores = ("rojo", "verde", "azul")
diccionario_edades = {"Juan": 25, "María": 30, "Carlos": 22}
conjunto_elementos = {1, 2, 3, 4, 5}

# Funciones
def saludar(nombre):
    return "¡Hola, " + nombre + "!"

mensaje_saludo = saludar("Estudiante")

# Entrada y Salida
nombre_usuario = input("Por favor, ingresa tu nombre: ")
print("Hola, " + nombre_usuario + "! Este es tu primer programa en Python.")

# Manejo de Errores
try:
    resultado_division = 0 / 0
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")
finally:
    print("Bloque 'finally': Este código se ejecuta siempre, haya o no haya errores.")

# Trabajo con Archivos
with open("archivo.txt", "w") as archivo:
    archivo.write("¡Hola desde un archivo!")

# Módulos y Bibliotecas
import math
raiz_cuadrada = math.sqrt(16)

# Programación Orientada a Objetos
class MiClase:
    def __init__(self, atributo):
        self.atributo = atributo

    def mostrar_atributo(self):
        print("El valor del atributo es:", self.atributo)

# Manejo de Cadenas (Strings)
longitud_cadena = len("Python")
mayusculas = "hola".upper()
minusculas = "HOLA".lower()
reemplazo = "python es divertido".replace("divertido", "increíble")