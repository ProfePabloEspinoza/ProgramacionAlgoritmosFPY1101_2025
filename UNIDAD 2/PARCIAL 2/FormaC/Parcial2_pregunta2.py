from random import uniform

n1 = int(input('Ingrese límite inferior: '))
n2 = int(input('Ingrese límite superior: '))

# Calcular el punto medio y el ajuste del 20% del rango
punto_medio = (n1 + n2) / 3
ajuste = (n2 - n1) * 0.2

# Generar el número aleatorio dentro del ajuste
num = round(punto_medio + uniform(-ajuste, ajuste))

flag = True
i1 = int(input('Intente adivinar: '))
if num == i1:
    print('Felicitaciones, adivinó en el primer intento.')
    flag = False
elif num < i1:
    print('El número es menor.')
else:
    print('El número es mayor.')

if flag:
    i2 = int(input('Intente de nuevo: '))
    if num == i2:
        print('Felicitaciones, adivinó en su segundo intento.')
        flag = False    
    else:
        if num < i2:
            print('El número es menor.')
        else:
            print('El número es mayor.')
        print("Te daré una pista:")
        d1 = abs(num - i1)
        d2 = abs(num - i2)
        if d1 < d2:
            print('El número que buscas está más cerca de', i1, 'que de', i2)
        elif d1 > d2:
            print('El número que buscas está más cerca de', i2, 'que de', i1)
        else:
            print('El número que buscas está a la misma distancia de', i1, 'que de', i2)
    
    if flag:
        i3 = int(input('Intente la última vez: '))
        if i3 == num:
            print('Felicitaciones, pudiste adivinar.')
        else:
            print('Perdiste.')
            print('El número era:', num)
