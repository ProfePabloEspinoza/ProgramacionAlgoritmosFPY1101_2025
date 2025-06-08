
""""
#Ejercicio 1

print('Bienvenido a DuocUc')
print('Vamos a calcular tus beneficios acorde a tu promedio y tu condición socioeconomica')

promedio = float(input('Ingrese su promedio final con el que salió del colegio: '))
decil = int(input('Ingrese su decil socioeconómico (1-10): '))

beneficio = 0
arancel = 2200000
matricula = 95000

if promedio > 6.5 and decil <= 2:
    beneficio = 0.25
    print('Usted tiene un 25% de descuento en su arancel')
elif promedio > 6.5 and 3 <= decil <= 4:
    beneficio = 0.18
    print('Usted tiene un 18% de descuento en el arancel')
elif 5.5 < promedio <= 6.5 and decil <= 2:
    beneficio = 0.15
    print('Usted tiene un 15% de descuento en el arancel')
elif 5.5 < promedio <= 6.5 and 3 <= decil <= 4:
    beneficio = 0.12
    print('Usted tiene un 12% de descuento en el arancel')
else:
    beneficio = 0
    print('Usted no tiene ningún descuento de arancel')



if decil <= 3 and promedio >= 6:
    beneficio_matricula = 0.17
    print('Además tiene un 17% de descuento en la matrícula')
elif decil <= 3:
    beneficio_matricula = 0.12
    print('Además tiene un 12% de descuento en la matrícula')
else:
    beneficio_matricula = 0
    print('Usted no tiene descuento en la matrícula')

arancel_total = arancel - (arancel * beneficio)
matricula_total = matricula - (matricula * beneficio_matricula)

print(f'El arancel total a pagar es:  ${arancel_total}')
print(f'El valor de la matricula total es: ${matricula_total}')

"""
#Ejercicio 2

import random

lim1 = float(input("Ingrese el límite inferior: "))   
lim2 = float(input("Ingrese el límite superior: "))

if lim1 >= lim2:
    print("El límite inferior debe ser menor que el límite superior.")
else:
    
    punto_medio = (lim1 + lim2) / 2
    ajuste = (lim2 - lim1) * 0.2
    num_aleatorio = int(random.uniform(punto_medio - ajuste , punto_medio + ajuste))
    num_aleatorio = max(int(lim1), min(num_aleatorio, int(lim2)))


    i = 3
    intento_realizado = 0
    intentos_previos = []
    intento = 0
    gano = False

    while intento_realizado < i:
        intento_realizado += 1
        intento = int(input('Advina el número: '))
        intentos_previos.append(intento)

        if intento == num_aleatorio:
            print('Ganaste')
            gano = True
            break
        else:
            if intento > num_aleatorio:
                print('Intentalo de nuevo: El número es menor')
            else:
                print('Intentalo de nuevo: El número es mayor')

        if intento_realizado == 2:

            diferencia_1 = abs(num_aleatorio - intentos_previos[0])
            diferencia_2 = abs(num_aleatorio - intentos_previos[1])

            if diferencia_1 < diferencia_2:
                print('Tu primer intento fue más cerca')
            elif diferencia_1 > diferencia_2:
                print('Tu segundo intento estuvo más cerca')
            else:
                print('Ambos intentos estuvieron igual de cerca')
    
if not gano:
    print('Perdiste')
    print(f'El número era {num_aleatorio}')

