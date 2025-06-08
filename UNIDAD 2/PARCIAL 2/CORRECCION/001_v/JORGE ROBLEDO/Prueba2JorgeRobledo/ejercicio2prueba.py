import random



print("Bienvenido a este juego, ingresa 2 numeros enteros, el primero tiene que ser menor que el segundo")
num1=int(input("Ingrese su primer numero:  "))
num2=int(input("Ingrese su segundo numero: "))

if num1>num2:
    print("ERROR")
    quit

punto_medio=num1+(num2/2)
ajuste=(num2-num1)*0.2
suma= punto_medio + ajuste
resta= punto_medio - ajuste
lista=[suma,resta]
numero_final=int(random.choice(lista))
contador_intentos=1
intentos=4

while contador_intentos< intentos:
    entrada=int(input("ingrese su intento: "))
    if entrada ==numero_final :
        print("Felicitaciones adivinaste")
        break
    elif entrada <numero_final and contador_intentos==2:
        
        contador_intentos=contador_intentos+1
        if entrada<(numero_final-1):
            print("Es mas")
        elif entrada<(numero_final+1):
            print("Es menos")
    elif entrada<numero_final and contador_intentos<2:
        contador_intentos=contador_intentos+1
    elif entrada> numero_final and contador_intentos==2:
      
        contador_intentos=contador_intentos+1
        if entrada>(numero_final-1):
            print("Es menos")
        elif entrada>=(numero_final+1) :
            print("Es menos")
    elif entrada> numero_final and contador_intentos <2:
        contador_intentos=contador_intentos+1
   
    if contador_intentos == intentos and entrada!=numero_final:
        print(f"ya lo intestaste 3 veces, adios. era{numero_final}")
        

