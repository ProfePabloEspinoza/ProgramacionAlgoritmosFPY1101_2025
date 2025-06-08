from random import randint
n1 = int(input('Ingrese limite inferior: '))
n2 = int(input('Ingrese limite superior: '))

num = randint(n1,n2)
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
        print('Felicitaciones, adivinó en su segundo intendo.')
        flag = False    
    else:
        if num < i2:
            print('El número es menor.')
        else:
            print('El número es mayor.')
        print("Te daré una pista:")
        d1 = abs(num-i1)
        d2 = abs(num-i2)
        if d1 < d2:
            print('El numero que buscas esta mas cerca de', i1, 'que de', i2)
        elif d1 > d2:
            print('El numero que buscas esta mas cerca de', i2, 'que de', i1)
        else:
            print('El numero que buscas esta a la misma distancia de', i1, 'que de', i2)
    
    if flag:
        i3 = int(input('Intente la ultima vez: '))
        if i3 == num:
            print('Felicitaciones, pudiste adivinar.')
        else:
            print('Perdiste.')
            print('El número era:', num)