entradas_disponibles = 70

while True:
    # Mostrar menú
    print("\n***** Cine Estrella *****") 
    print("Bienvenido al sistema de venta de entradas del Cine Estrella")
    print("1. Ver entradas disponibles")
    print("2. Comprar entradas")
    print("3. Salir")

    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        print(f"Entradas disponibles: {entradas_disponibles}")
    
    elif opcion == "2":
        try:
            cantidad = int(input("¿Cuántas entradas desea comprar?: "))
            if cantidad <= entradas_disponibles and cantidad > 0:
                entradas_disponibles -= cantidad
                print(f"Compra exitosa. Quedan {entradas_disponibles} entradas.")
            else:
                print("No hay suficientes entradas disponibles o número inválido.")
        except:
            print("Debe ingresar un número entero válido.")
    
    elif opcion == "3":
        print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
