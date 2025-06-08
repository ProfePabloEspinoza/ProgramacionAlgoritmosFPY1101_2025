"""
# 1 
while True:
    try: 
        cantidad = int(input('Cuantos códigos va a verificar?....'))
        break
    except:
        print('Ingrese solo numeros..')
        
        

valido = 0
invalido = 0

for i in range(1, cantidad + 1):
    
    while True:
        try: 
            codigo = int(input(f'Ingrese el codigo {i} a verificar?....'))
            
            if codigo > 10:
                break
            else:
                print('Ingrese un codigo mayor a 10.')
        except:
            print('Ingrese solo numeros..')
    
    
    contador = 0
    
    for j in range(1, codigo + 1):
        if codigo % j == 0:
            contador = contador + 1
            
    
    if contador == 3:
        print(f'el codigo {codigo} ES VÁLIDO ')
        valido =+ 1
    else: 
        print(f'el codigo {codigo} ES INVÁLIDO ')
        invalido =+ 1
             
    
    
# MOSTRAMOS LOS RESULTADOS

print(f'\n Se ingresaron {valido} codigos VALIDOS')
print(f'\n Se ingresaron {invalido} codigos INVALIDOS')

"""

# 2

mayor = None
menor = None


while True:
    
    print('1.- ingrese temp')
    print('2- cual temp es mayor')
    print('3- cual temp es menor')
    print('4.- Salir')
    
    opcion = input('Ingrese una opcion del menu: ')
    
    if opcion == '1':
        while True:
            try:
                temp = int(input('Ingrese una temperatura entre -50 y 50 grados: '))
                
                if (temp < -50 or temp > 50):
                    print('Ingrese una temp entre -50 y 50 grados')
                else:
                    if mayor is None:
                        mayor = temp
                        menor = temp
                    else:
                        if temp > mayor:
                            mayor = temp
                        if temp <  menor:
                            menor = temp
                        
                        print('Temperatura registrada')     
                        break                 
                        
                
            except:
                print('Ingrese solo numeros....')
                
    elif opcion == '2':
        if mayor == None:
            print('Debe ingresar una temnperatura antes, vaya a la op 1: ')
        else:
            print(f'La temperatura mnayor es: {mayor}')
            
    elif opcion == '3':
        if menor == None:
            print('Debe ingresar una temnperatura antes, vaya a la op 1: ')
        else:
            print(f'La temperatura menor  es: {menor}')
            
    elif opcion == '4':
        print('Saliendo....')
        break
    
    else:
        print('Opcion invalida...')

print('Fin del programa...')
            
    

