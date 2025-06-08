

num1 = int(input("Ingrese el primer número (debe ser el menor): "))
num2 = int(input("Ingrese el segundo número (debe ser el mayor): "))

if num1 >= num2:
    print("Erroneo: El primer número debe ser menor que el segundo.")
else:
   
    punto_medio = (num1 + num2) / 2

    ajuste = (num2 - num1) * 0.2


    if (num1 + num2) % 2 == 0:
        numero_secreto = punto_medio + ajuste
    else:
        numero_secreto = punto_medio - ajuste

    numero_secreto = round(numero_secreto)

    print("Adivina, tiienes 3 intentos.")


    intento1 = int(input("Intento 1: "))
    if intento1 == numero_secreto:
        print("Genio, le atinaste a la primera.")
    else:
        if intento1 < numero_secreto:
            print("El número secreto es MAYOR.")
        else:
            print("El número secreto es MENOR.")

        intento2 = int(input("Intento 2: "))
        if intento2 == numero_secreto:
            print("Brutal, adivinaste a la segunda.")
        else:
            if intento2 < numero_secreto:
                print("El número secreto es MAYOR.")
            else:
                print("El número secreto es MENOR.")

    #Hasta aqui llegue :( 
