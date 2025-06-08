import random
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))

if numero1<numero2:
    promedio=(numero1+numero2)/2
    ajuste=(numero2-numero1)*0.2
    restarandom=(promedio-ajuste)
    sumarandom=(promedio+ajuste)
    limite = random.choice([sumarandom, restarandom])
    aleatorio = random.randint(0, int(limite))
    print("intenta adivinar el numero generado aleatoriamente", aleatorio)
    # aqui coloco visible el numero aleatorio para que usted vea que efectivamente se genero aleatoriamente
    #si no lo quiere ver, lo borro y el juego se hace mas interesante

    primerintento=int(input("ingrese el primer intento: "))
    if primerintento==aleatorio:
        print("felicitaciones, adivinaste el numero exacto")
    elif primerintento<aleatorio:
        print("el numero es mayor")
    elif primerintento>aleatorio:
        print("el numero es menor")

    segundointento=int(input("ingrese el segundo intento: "))
    if segundointento==aleatorio:
        print("felicitaciones, adivinaste el numero exacto")
    elif segundointento<aleatorio:
        print("el numero es mayor")
    elif segundointento>aleatorio:
        print("el numero es menor")

    if abs(primerintento - aleatorio) < abs(segundointento - aleatorio):
        print((primerintento), "está más cerca que ", (segundointento))
    elif abs(segundointento - aleatorio) < abs(primerintento - aleatorio):
        print((segundointento), " está más cerca que ", (primerintento))
    else:
        print("están a la misma distancia")

    tercerintento=int(input("ingrese el tercer intento: "))
    if tercerintento==aleatorio:
        print("felicitaciones, adivinaste el numero exacto")
    else:
        print("no adivinaste el numero")
        print("el monto es: ", aleatorio)
else:
    print("El primer numero no es menor que el segundo numero")


