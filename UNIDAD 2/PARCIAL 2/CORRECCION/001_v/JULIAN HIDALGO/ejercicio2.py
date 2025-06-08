num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero (debe ser mayor que el primero): "))

if num1 >= num2:
    print("El primer numero debe ser menor que el segundo. Intenta nuevamente.")
else:
    punto_medio = (num1 + num2) / 2
    ajuste = (num2 - num1) * 0.2
    random_num = punto_medio - ajuste

    intento1 = float(input("Ingresa un número: "))

    if intento1 == random_num:
        print("Felicitaciones, pudiste adivinar")
    else:
        if intento1 < random_num:
            print("El número es mayor.")
        elif intento1 > random_num:
            print("El número es menor.")
        
        #INTENTO NUMERO 2
        intento2 = float(input("Intenta nuevamente, te quedan 2 intentos: "))
        
        if intento2 == random_num:
            print("Felicitaciones, pudiste adivinar")
        else:
            if intento2 < random_num:
                print("El numero es mayor.")
            elif intento2 > random_num:
                print("El numero es menor.")

            if (intento1 - random_num) < (intento2 - random_num):
                print(f"El numero {intento1} esta cerca.")
            else:
                print(f"El numero {intento2} esta cerca.")
            
            #INTENTO NUMERO 3
            intento3 = float(input("Intenta nuevamente, es tu ultimo intento: "))

            if intento3 == random_num:
                print("Felicitaciones, pudiste adivinar")
            else:
                print(f"Perdiste, el numero era: {random_num}.")
