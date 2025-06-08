#rango

num1 = int(input("Ingrese limite inferior: "))
num2 = int(input("Ingrese limite superior: "))

if num1 > num2:
    print("el primer numero debe ser menor que el segundo numero")
else:
    num_medio = (num1 + num2) / 2
    num_ajuste = (num2 - num1) * 0.2

    print({num_ajuste})
    for intento in [1,4]:
            adivinar = int(input("Intente adivinar: "))
            if intento == 1 :
                if adivinar == num_medio :
                        print("Felicitaciones, adivino en el primer intento")
                else:
                    if adivinar > num_medio:
                        print(f"El numero es menor")
                    else: 
                        print(f"El numero es mayor")
            elif intento == 2 :
                adivinar = int(input("Intente de nuevo: "))
                if adivinar == num_medio:
                    print(f"Felicitaciones, pudiste adivinar")
                else:
                    if adivinar > num_medio:
                        print(f"Te doy una pista el numero es menor")
                        print(f"El numero que buscas esta mas cerca del {adivinar} que de {adivinar}")
                    elif adivinar < num_medio:
                        print(f"Te doy una pista el numero es mayor")
                        print(f"El numero que buscas esta mas cerca del {adivinar} que de {adivinar}")
            elif intento == 3 :
                adivinar = int(input("Intente la ultimo vez: "))
                if adivinar == num_medio:
                    print(f"Felicitaciones, pudiste adivinar")
                else:
                    print(f"Perdiste. El numero era: {num_medio}")

