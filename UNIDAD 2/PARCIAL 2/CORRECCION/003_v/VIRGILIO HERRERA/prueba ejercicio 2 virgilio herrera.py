num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 < num2:
    numero_generado = (num1 + num2) // 2 

    print("inicia el juego: tienes 3 intentos para adivinar el número.")

    respuesta_1 = int(input("Intento 1: Ingrese su número: "))
    if respuesta_1 == numero_generado:
        print("felicitaciones, pudiste adivinar")
    else:
        print("Incorrecto. El número es mayor." if respuesta_1 < numero_generado else "Incorrecto. El número es menor.")

        respuesta_2 = int(input("Intento 2: Ingrese su número: "))
        if respuesta_2 == numero_generado:
            print("¡Felicitaciones, pudiste adivinar!")
        else:
            print("Incorrecto. El número es mayor." if respuesta_2 < numero_generado else "Incorrecto. El número es menor.")

            print(f"Pista: El número correcto está cerca de {respuesta_1} o {respuesta_2}.")

            respuesta_3 = int(input("Intento 3: Ingrese su número: "))
            if respuesta_3 == numero_generado:
                print("¡Felicitaciones, pudiste adivinar!")
            else:
                print("Incorrecto. El número es mayor." if respuesta_3 < numero_generado else "Incorrecto. El número es menor.")
                print(f"Perdiste. El número correcto era {numero_generado}.")
else:
    print("Error: El primer número debe ser menor que el segundo.")