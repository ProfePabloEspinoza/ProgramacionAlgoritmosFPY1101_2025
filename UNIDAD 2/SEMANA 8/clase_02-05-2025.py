"""
1. ¿Puede entrar a la película?
Objetivo: Practicar condiciones simples (if/else) y operadores 
de comparación.
Enunciado: Crea un programa que pregunte al usuario su edad. 
Si tiene 13 años 
o más, puede entrar a ver la película. Si es menor de 13,
 muestra un mensaje que diga 'Debes estar acompañado 
 por un adulto'.


edad = int(input('Ingrese su edad: '))

if edad >= 13:
    print('Puede ver la pelicula')
else:
    print('Debes venir acompañado por un adulto')



2.- Haz un programa que pregunte si tienes más de 21 años y si 
tienes una casa con patio. Si ambas condiciones se cumplen, 
puedes adoptar un perro. En caso contrario, el programa 
debe mostrar 'No cumples con los requisitos para adoptar'.




edad = int(input('Ingrese su edad: '))
tiene_patio = input('si/no')

if (edad > 21) and (tiene_patio == 'si'):
    print('Puedes adoptar al perro.')
else:
    print('No cumples con los requisitos para adoptar')



Para entrar al Club de Aventureros, necesitas tener al 
menos 15 años y traer el permiso firmado por tus padres.



edad = int(input('Ingrese su edad: '))
permiso = input('Tiene permiso de los padres (s/n): ') == 's'

if (edad >= 15) and permiso:
    print('Bienvenido al club')
else: 
    print('No puede entrar.')



4.- Un cine da descuento si el cliente es estudiante 
o mayor de 60 años.



es_estudiante = input('¿Eres estudiante? (s/n): ') == 's'
edad = int(input('¿Cuantos años tienes?: '))

if es_estudiante or edad >= 60:
    print('Tienes descuentos en el cine')
else:
    print('No tienes descuentos')



5.- Haz un programa que reciba el nivel de experiencia 
(1-100) y diga qué tipo de personaje es:

- Nivel 1 a 20 → “Principiante”
- Nivel 21 a 50 → “Intermedio”
- Nivel 51 a 80 → “Avanzado”
- Nivel 81 a 100 → “Maestro”


nivel = int(input('Ingrese tu nivel de experiencia (1-100): '))

if nivel <= 20:
    print('Eres un Principiante')
elif nivel <= 50:
    print('Eres un Intermedio')
elif nivel <= 80:
    print('Eres un Avanzado')
else: 
    print('Eres un Maestro')

"""




           
           





