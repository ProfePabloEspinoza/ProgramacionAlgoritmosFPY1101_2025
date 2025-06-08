numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

if numero1 >= numero2:
    print("El primer numero debe ser menor que el segundo.")
else:
    punto_medio = (numero1 + numero2) / 2
    ajuste = (numero2 - numero1) * 0.2
    paso = (numero2 - numero1) // 10  

    if (numero2 - numero1) % 2 == 0:
        numero_secreto = int(punto_medio + ajuste - paso)
    else:
        numero_secreto = int(punto_medio - ajuste + paso)
        print("Tienes 3 intentos para adivinar el numero.")
    intento1 = int(input("Intento 1: Ingrese su numero: "))

    if intento1 == numero_secreto:
        print("Felicidades adivinaste ")
    else:
        if intento1 < numero_secreto:
            print("El numero es mayor")
        else:
            print("El numero es menor")
            intento2 = int(input("Intento 2: Ingrese su numero: "))
        if intento2 == numero_secreto:
            print("Felicidades adivinaste")
        else:
            if intento2 < numero_secreto:
                print("El numero es mayor")
            else:
                print("El numero es menor")

            if abs(numero_secreto - intento2) < abs(numero_secreto - intento1):
                print(f"Pista, El numero {intento2} estuvo mas cerca que {intento1}.")
            else:
                print(f"Pista, El numero {intento1} estuvo mas cerca que {intento2}.")

            intento3 = int(input("Intento 3: Ingrese su numero: "))

            if intento3 == numero_secreto:
                print("Felicidades adivinaste")
            else:
                print(f"Perdiste. El numero correcto era {numero_secreto}.")