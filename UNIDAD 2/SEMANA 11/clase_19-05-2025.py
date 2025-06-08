"""
a = 4
b = 0
c = a / b

print(f'El resultado de la division es: {c}')

###################################

a = 4
b = "4"
c = a + b

print(f'El resultado de la suma es: {c}')

###############################################
try:

    a = 4
    b = 0
    d = 4
    e = '4'    
    c = a / b
    print(f'El resultado de la division es: {c}')

    f = d + e
    print(f'La suma es: {f}')   

except ZeroDivisionError:
    print('No puede dividir por cero...')

except TypeError:
    print('No puede sumar numeros con string')

except:
    print('Aqui cualquier tipo de error')

finally: # el finally es opcional y siempre se ejecutará
          # exista un error o no...
          print('siempre se ejecuta')

"""

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
            print(f'La resta es: {num1 - num2}')
        except ZeroDivisionError:
            print('No puede dividir por cero')

    elif opcion == "4":
        print('saliendo....')
        break
    else: 
        print('Elija una opcion Valida.')
    
    




        




