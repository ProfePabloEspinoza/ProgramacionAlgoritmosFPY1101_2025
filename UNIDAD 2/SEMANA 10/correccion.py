# Inicialización de variables
mayor = None
menor = None

# Menú principal
while True:
    print("\n*** REGISTRO DE TEMPERATURAS ***")
    print("1. Ingresar temperatura.")
    print("2. Mostrar temperatura más alta registrada.")
    print("3. Mostrar temperatura más baja registrada.")
    print("4. Salir del programa.")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            try:
                temp = int(input("Ingrese temperatura: "))
                if temp < -50 or temp > 50:
                    print("La temperatura debe estar entre -50 y 50 grados.")
                else:
                    if mayor is None:
                        mayor = temp
                        menor = temp
                    else:
                        if temp > mayor:
                            mayor = temp
                        if temp < menor:
                            menor = temp
                    print("Temperatura registrada.")
                    break
            except:
                print("Debe ingresar un número entero.")

    elif opcion == "2":
        if mayor is None:
            print("No se han registrado temperaturas aún.")
        else:
            print(f"La temperatura más alta registrada es: {mayor}°C")

    elif opcion == "3":
        if menor is None:
            print("No se han registrado temperaturas aún.")
        else:
            print(f"La temperatura más baja registrada es: {menor}°C")

    elif opcion == "4":
        print("Programa finalizado. Gracias por usar el sistema.")
        break

    else:
        print("Debe seleccionar una opción válida (1 a 4).")