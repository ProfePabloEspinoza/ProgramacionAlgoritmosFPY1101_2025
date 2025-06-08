# Precio base de la entrada
precio_base = 15000.0
precio_final = precio_base # Inicializar precio final

# Solicitar datos
edad = int(input('Ingrese la edad del asistente: '))
es_estudiante_str = input('¿Es estudiante? (si/no): ').lower() # Convertir a minúsculas

# Aplicar descuento por edad usando if/elif/else
descuento_edad = 0.0 # Variable para guardar el porcentaje de descuento por edad

if edad >= 0 and edad <= 12:
    # Niño
    descuento_edad = 0.60
elif edad >= 13 and edad <= 17:
    # Adolescente
    descuento_edad = 0.30
elif edad >= 18 and edad <= 64:
    # Adulto
    descuento_edad = 0.0
elif edad >= 65:
    # Adulto Mayor
    descuento_edad = 0.50
else:
    # Edad inválida (opcional manejar)
    print("Edad ingresada no válida.")
    descuento_edad = 0.0 # O podrías terminar el programa

# Calcular precio después del descuento por edad
precio_con_desc_edad = precio_base * (1 - descuento_edad)

# Aplicar descuento adicional por estudiante si cumple las condiciones
# Usamos if anidado para verificar ambas condiciones (respuesta "si" y rango de edad)
precio_final = precio_con_desc_edad # Por defecto, el precio final es el ajustado por edad

if es_estudiante_str == "si":
    if edad >= 13 and edad <= 25:
        # Solo aplica si es estudiante Y está en el rango de edad correcto
        descuento_estudiante = 0.10
        # El descuento se aplica sobre el precio ya ajustado por edad
        precio_final = precio_con_desc_edad * (1 - descuento_estudiante)
    # Si responde "si" pero no está en el rango de edad, no se hace nada extra,
    # el precio_final sigue siendo precio_con_desc_edad

# Si responde "no", tampoco se hace nada extra.

# Mostrar resultado final
print('El precio final de la entrada es: $', precio_final)