
#Ejercicio 1
promedio = float(input('Ingrese su promedio: \n'))
decil = int(input('Ingrese su decil(1-10): \n'))

arancel = 2200000
matricula = 95000

if promedio > 6.5:
    if decil == 1 or decil == 2:
        arancel = arancel - (arancel * 0.25)
    elif decil == 3 or decil == 4:
        arancel = arancel - (arancel * 0.18)
elif promedio <= 6.5 and promedio >= 5.5:
    if decil == 1 or decil == 2:
        arancel = arancel - (arancel * 0.15)
    elif decil == 3 or decil == 4:
        arancel = arancel - (arancel * 0.12)

if decil == 1 or decil == 2 or decil == 3:
    matricula = matricula - (matricula * 0.12)
    if promedio >= 6.0:
        matricula = matricula - (matricula * 0.05)


print(f'El valor del arancel es: ${arancel}\n')
print(f'El valor de la matricula es: ${matricula}\n')


#Ejercicio 2 
import random
ok = False

while ok == False:
    num1 = int(input('Ingrese limite inferior: \n'))
    num2 = int(input('Ingrese limite superior: \n'))
    if num1 < num2:
        ok = True
    else: 
        print('Error. Segundo número debe ser mayor al primero. Intente nuevamente \n')

punto_medio = num1+num2/2 
print(punto_medio)
ajuste = (num2 - num1)* 0.2
print(ajuste)
suma = punto_medio + ajuste
resta = punto_medio - ajuste
operadores = (suma, resta)
num_final = random.choice(operadores)
print(num_final)

i = 3
while i > 0:
    guess1 = float(input('Intente adivinar: \n'))
    if guess1 == num_final:
        print('Felicitaciones, pudiste adivinar al primer intento')
        break
    else:
        i = i - 1
        if guess1 > num_final:
            print('El número es menor\n')
        else: 
            print('EL número es mayor\n')            
        guess2 = float(input('Intente adivinar de nuevo: \n'))
        if guess2 == num_final:
            print('Felicitaciones, pudiste adivinar al segundo intento')
            break
        else:
            i = i - 1
            dist1 = abs(guess1 - num_final)
            dist2 = abs(guess2 - num_final)            
            if guess2 > num_final:
                print('El número es menor\n')
            else: 
                print('EL número es mayor\n')
                if dist1 > dist2:
                    print('Te daré una pista:')
                    print(f'El número que buscas está mas cerca del {guess2} que de {guess1}\n')
                else: 
                    print('Te daré una pista:')
                    print(f'El número que buscas está mas cerca del {guess1} que de {guess2}\n')
                guess3 = float(input('Intente adivinar por última vez: \n'))
                if guess3 == num_final:
                    print('Felicitaciones, pudiste adivinar al tercer intento')
                    break
                else:
                    i = i - 1
                    print('Perdiste')
                    print(f'El número era: {num_final}')
            



