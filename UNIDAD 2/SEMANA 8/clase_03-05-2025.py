"""
1.- Crea un programa que pregunte al usuario su edad. 
Si tiene 13 años o más, puede entrar a ver la película.
 Si es menor de 13, muestra un mensaje que diga 
 'Debes estar acompañado por un adulto'.

edad = input('Ingrese su edad: ')
edad = int(edad)

if edad >= 13:
    print('Puedes ver la pelicula')
else:
    print('debes venir acompañado por un adulto')

--------------------------------------------------------
 2.- Haz un programa que pregunte si tienes más de 21 años 
 y si tienes una casa con patio. Si ambas condiciones 
 se cumplen, puedes adoptar un perro. En caso contrario, 
 el programa debe mostrar 'No cumples con los requisitos 
 para adoptar'.

edad = int(input('Ingrese su edad: '))
tiene_patio = input('Tienes patio (S/N): ')
tiene_patio = tiene_patio.upper()

if (edad > 21) and (tiene_patio == 'S'):
    print('puedes adoptar un perrito')
else:
    print('No cumples los requisitos para adoptar.')
-----------------------------------------------------------------
3.- Un cine da descuento si el cliente 
es estudiante o mayor de 60 años.

4.- Crea un programa para determinar si un estudiante 
puede ir a una excursión escolar. 
Para poder ir, el estudiante debe cumplir todos los 
siguientes requisitos:
* Tener el permiso firmado por los padres.
* Haber pagado la cuota de la excursión.
* No tener asignaturas suspendidas (calificación reprobatoria).
* Tener un buen registro de comportamiento.


print('Evaluacion de requisitos para excursion')
print('-' * 40)

permiso = input('Tienes permiso de tus padres (s/n): ').lower()
cuotas = input('Tienes las cuotas pagadas (s/n): ').lower()
notas = input('tienes todos las notas azules (s/n): ').lower()
comportamiento = input('te sabes comportar (s/n): ').lower()

if (permiso == 's' and
    cuotas == 's' and
    notas == 's' and
    comportamiento == 's'):

    print('Puedes ir al paseo')

else:
    print('No puedes ir al paseo porque no cumples lo siguiente: ')

    if permiso != 's':
        print('No tienes permiso de tus padres.')
    if cuotas != 's':
        print('no tienes las cuotas pagadas.')
    if notas != 's':
        print('no tienes buenas notas.')
    if comportamiento != 's':
        print('no te sabes comportar.')

-------------

5.- Haz un programa que reciba el nivel de experiencia (1-100) 
y diga qué tipo de personaje es:
- Nivel 1 a 20 → “Principiante”
- Nivel 21 a 50 → “Intermedio”
- Nivel 51 a 80 → “Avanzado”
- Nivel 81 a 100 → “Maestro”

"""
nivel = int(input('Ingresa tu nivel entre (1-100): '))

if nivel <= 20:
    print('Principiante')
elif nivel <= 50:
    print('intermedio')
elif nivel <= 80:
    print('avanzado')
elif nivel <= 100:
    print('maestro')
else:
    print('estas fuera de rango (1-100)')




