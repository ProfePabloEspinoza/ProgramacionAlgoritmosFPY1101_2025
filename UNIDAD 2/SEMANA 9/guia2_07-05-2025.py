
precio_base = 15000


# Solicitamos los Datos
edad = int(input('Ingresa la edad del solicitante: '))
es_estudiante = input('Es estudiante? (SI/NO): ').upper()

descuento_edad = 0.0

# APLICAR DESCUENTO POR EDAD

if edad >= 0 and edad <= 12:
    # niño
    descuento_edad = 0.60
elif edad >= 13 and edad <= 17:
    # adolecente
    descuento_edad = 0.30
elif edad >= 18 and edad <= 64:
    # adulto
    descuento_edad = 0.0
elif edad >= 65 and edad <= 120:
    # adulto mayor
    descuento_edad = 0.50
else:
    print('Edad no válida')
    descuento_edad = 0.0

# esto aplica cuando la persona no es estudiante
# calculamos precio despues del descuento por edad
precio_con_desc_edad = precio_base * (1 - descuento_edad)

precio_final = precio_con_desc_edad

if es_estudiante == 'SI':
    if edad >= 13 and edad <= 25:
        descuento_estudiante = 0.10

        precio_final = precio_con_desc_edad * (1 - descuento_estudiante)

print(f'El precio final de la entrada es: ${precio_final}')



