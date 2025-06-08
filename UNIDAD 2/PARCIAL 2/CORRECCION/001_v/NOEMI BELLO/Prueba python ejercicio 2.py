import random

def mi_juego ():
    print("Bienvenido al juego de las adivinanzas")


def mi_juego():
    print("Piensa en un numero del 1 al 100 para adivinarlo")

    num1 = int(input("Ingrese el primer número del rango (menor): "))
    num2 = int(input("Ingrese el segundo número del rango (mayor): "))

    if num1 >= num2:
        print("El primer numero debe ser menor que el segundo")
        return

    numero_secreto = random.randint(num1, num2)
    intento = 3

    while intento > 0:
        adivinanza = int(input(f"Te quedan {intento} intentos. Adivina el numero: "))
        if adivinanza == numero_secreto:
            print("Felicidades, adivinaste el numero")
            return
        elif adivinanza < numero_secreto:
            print("El numero es mayor")
        else:
            print("El numero es menor")
        intento -= 1

    print(f"Lo siento, no adivinaste el numero. El numero secreto era {numero_secreto}")

mi_juego()
