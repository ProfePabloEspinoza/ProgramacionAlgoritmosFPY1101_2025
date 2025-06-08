"""
try: 

    d = 4
    e = "5"
    f = d + e
    print(f'El resultado de la suma: {f}')
    
except ZeroDivisionError:
    print(f'No se puede dividor por cero...')
except:
    print('aqui va cualquier tipo de error')

finally:
    print('este codigo siempre se va a ocupar exista error o no..')


try:
    a = 4
    b = 0
    c = a / b
    print(f'El resultado de la division es: {c}')   

except TypeError:
    print(f' No puede sumar numeros con caracteres..')

except:
    print('aqui va cualquier tipo de error')

finally:
    print('este codigo siempre se va a ocupar exista error o no..')

"""

# MENU

while True:
    print('Menu calculadora...')
    print('1.- Sumar')
    print('2.- Restar')
    print('3.- Mutiplicar')
    print('4.- Dividir')
    print('5.- Salir')

    opcion = input('Ingrese una opcion: ')

    if opcion == '1':
        print('sumar')

        try:
            num1 = int(input('Ingrese numero 1: '))
            num2 = int(input('Ingrese numero 2: '))
            print(f'La suma entre {num1} + {num2} = {num1 + num2}')
        except TypeError:
            print('No puede sumar numero con letras....')
        

    elif opcion == '2':
        print('restar')
        try:
            num1 = int(input('Ingrese numero 1: '))
            num2 = int(input('Ingrese numero 2: '))
            print(f'La resta entre {num1} - {num2} = {num1 - num2}')
        except TypeError:
            print('No puede sumar numero con letras....')

    elif opcion == '3':
        print('mutiplicar')
        try:
            num1 = int(input('Ingrese numero 1: '))
            num2 = int(input('Ingrese numero 2: '))
            print(f'La multiplicacion entre {num1} x {num2} = {num1 * num2}')
        except TypeError:
            print('No puede sumar numero con letras....')
    
    elif opcion == '4':
        print('dividir')
        try:
            num1 = input('Ingrese numero 1: ')
            num2 = input('Ingrese numero 2: ')
            print(f'La division entre {num1} / {num2} = {int(num1 / num2) }')
        
        except ZeroDivisionError:
            print('No se puede dividir por cero.')
       
        except:
            print('No puede sumar numero con letras....')

    
    elif opcion == '5':
        print('saliendo...')
        break
    else:
        print('Elija una opción válida')

        



    



