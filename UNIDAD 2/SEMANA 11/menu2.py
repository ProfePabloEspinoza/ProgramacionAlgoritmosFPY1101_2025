#### Menu

while True:

    print('Menu de opciones:')
    print('1.- Realizar suma:')
    print('2.- Realizar Resta')
    print('3.- Realizar Division')
    print('4.- salir')

    opcion = input('Seleccione una opcion (1-2-3): ')

    if opcion == "1":
        print('Opcion de suma:')
        # aqui va el codigo que sume
        num1 = int(input('Ingrese numero 1: '))
        num2 = int(input('Ingrese numero 2:'))
        print(f'La suma es: {num1 + num2}')

    elif opcion == "2":
        print('Opcion de resta:')
        # aqui va el codigo que reste
        num1 = int(input('Ingrese numero 1: '))
        num2 = int(input('Ingrese numero 2:'))
        print(f'La resta es: {num1 - num2}')
    
    elif opcion == "3":
        try:
            print('Opcion de dividir:')
            num1 = int(input('Ingrese numero 1: '))
            num2 = int(input('Ingrese numero 2:'))
            print(f'La division es: {num1 / num2}')
        except ZeroDivisionError:
            print('No puede dividir por cero')

    elif opcion == "4":
        print('saliendo....')
        break
    else: 
        print('Elija una opcion Valida.')
    
    
