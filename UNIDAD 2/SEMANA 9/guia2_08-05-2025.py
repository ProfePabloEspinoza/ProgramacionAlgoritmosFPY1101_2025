PRECIO_BASE = 15000

edad = int(input('Ingrese la edad del asistente: '))
es_estudiante = input('¿Es usted estudiante?: (si/no)').lower()

descuento_edad = 0.0

# aplico el descuento segun la edad

if edad >= 0 and edad <= 12:
    # niño
    descuento_edad = 0.60
elif edad >= 13 and edad <= 17:
    # adolecente
    descuento_edad = 0.30
elif edad >= 18 and edad <= 64:
    # adultos
    descuento_edad = 0.0
elif edad >= 65 and edad <= 110:
    # adulto mayor
    descuento_edad = 0.50
else:
    print('coloque una edad válidad')
    descuento_edad = 0.0

precio_con_desc_edad = PRECIO_BASE * (1 - descuento_edad)

precio_final = precio_con_desc_edad

if es_estudiante == 'si':
    if edad >= 13 and edad <= 25:
        descuento_estudiante = 0.10

        precio_final = precio_con_desc_edad * (1 - descuento_estudiante)


print(f'el precio final es: ${precio_final}')













