#ejercicio 1
ARANCEL = 2200000
MATRICULA = 95000

promedio = float(input('Ingrese su promedio: '))
cond_soc = int(input('Ingrese su decil (1-10): '))

if promedio > 6.5:
    if cond_soc <= 2:
        ARANCEL *= 0.75
    elif 3 <= cond_soc <= 4:
        ARANCEL *= 0.82
elif 5.5 < promedio <= 6.5:
    if cond_soc <= 2:
        ARANCEL *= 0.85
    elif 3 <= cond_soc <= 4:
        ARANCEL *= 0.88

ARANCEL = int(ARANCEL)

if cond_soc <= 3:
    if promedio >= 6.0:
        MATRICULA *= 0.83
    else:
        MATRICULA *= 0.88

MATRICULA = int(MATRICULA)

print(f'El valor del arancel es ${ARANCEL}')
print(f'El total de la matrícula es ${MATRICULA}')

#ejercicio2
primer_numero = int(input('Ingrese limite inferior (numero entero) '))
segundo_numero = int(input('Ingrese limite superior (numero entero) '))

if primer_numero > segundo_numero:
    print('Ingrese bien los numeros')
elif primer_numero < segundo_numero:
    punto_medio = (primer_numero + segundo_numero)/2
    punto_medio = int(punto_medio)
    ajuste = (segundo_numero - primer_numero) * 0.2
    ajuste = int(ajuste)
    num_secreto = punto_medio + ajuste
    contador_int = 2
    intento1 = int (input (f'Intente adivina el numero, le quedan {contador_int} intentos '))
    if intento1 == num_secreto:
        print ('Felicitaciones, pudiste adivinar')
    else:
        contador_int  = contador_int - 1
        if intento1 == num_secreto:
            print ('Felicitaciones, pudiste adivinar')
        else:
            if intento1 > num_secreto:
                print ('El numero secreto es menor')
            else:
                print ('El numero secreto es mayor')
            intento2 = int (input (f'Intente adivina el numero, le quedan {contador_int} intentos '))
            if intento2 == num_secreto:
                    print ('Felicitaciones, pudiste adivinar')
            else:
                contador_int  = contador_int - 1
                if intento2 > num_secreto:
                    print ('El numero secreto es menor')
                else:
                    print ('El numero secreto es mayor')
                intento3 = int (input (f'Intente adivina el numero, le quedan {contador_int} intentos '))
                
                if intento3 == num_secreto:
                    print ('Felicitaciones, pudiste adivinar')
                else:
                    contador_int  = contador_int - 1
                    if intento3 > num_secreto:
                        print ('El numero secreto es menor')
                        print ('Perdiste')
                    else:
                        print ('El numero secreto es mayor')
                        print ('Perdiste')

