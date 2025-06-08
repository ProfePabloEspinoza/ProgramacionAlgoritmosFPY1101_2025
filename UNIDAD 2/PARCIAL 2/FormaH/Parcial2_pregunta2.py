from random import randint

# Ingresar límites del rango
n1 = int(input('Ingrese límite inferior: '))
n2 = int(input('Ingrese límite superior: '))

# Validar que el primer número sea menor que el segundo
if n1 >= n2:
    print("Error: El límite inferior debe ser menor que el límite superior.")
else:
    # Generar el número aleatorio dentro del rango y ajustarlo a múltiplo de 4
    num = randint(n1, n2)
    num = (num // 4) * 4  

    # Primer intento
    i1 = int(input('Intente adivinar: '))
    if i1 == num:
        print('Felicitaciones, adivinaste en el primer intento.')
    else:
        print('El número es menor.' if i1 > num else 'El número es mayor.')

        # Segundo intento
        i2 = int(input('Intente de nuevo: '))
        if i2 == num:
            print('Felicitaciones, adivinaste en el segundo intento.')
        else:
            print('El número es menor.' if i2 > num else 'El número es mayor.')

            # Pista entre los dos intentos previos
            print("Te daré una pista:")
            if abs(num - i1) < abs(num - i2):
                print(f'El número que buscas está más cerca de {i1}.')
            else:
                print(f'El número que buscas está más cerca de {i2}.')

            # Tercer intento
            i3 = int(input('Intente la última vez: '))
            if i3 == num:
                print('Felicitaciones, adivinaste.')
            else:
                print(f'Perdiste. El número era: {num}')

