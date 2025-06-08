mayor = -1
menor = 101
contador = 0
while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Ingresar número.")
    print("2. Mostrar mayor.")
    print("3. Mostrar total de número ingresados.")
    print("4. Terminar programa.")
    op = input("Elija opción: ")
    if op == "1":
        while True:
            try:
                n = int(input("Ingrese numero entre 0 y 100: "))
                if n >= 0 and n <= 100:
                    print("Ingreso exitoso")    
                    break
                else:
                    print("Debe ingresar un número entre 0 y 100!!")
            except:
                print("Debe ingresar un numero entero!!")     
        if n > mayor:
            mayor = n
        contador += 1
    elif op == "2":
        if mayor == -1:
            print("No se han ingresado números.")
        else:
            print("El número mayor hasta el momento es:", mayor)
    elif op == "3":
        if contador == 0:
            print("No se han ingresado números para calcular el total.")
        else:
            print(f"El total de los números ingresados es: {contador}")
    elif op == "4":
        print("Fin del programa. Adiós.")
        break
    else:
        print("Debe ingresar una opción valida.")