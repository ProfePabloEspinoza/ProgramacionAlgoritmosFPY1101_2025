

## 1

while True:
    try: 
        cantidad = int(input('Cuantos codigos va a verificar?: '))
        break
    except:
        print('Ingrese solo numeros....')

#print('Estoy fuera del while y puedo seguir con lo que indica el compañero...')

valido = 0
invalido = 0

for i in range(1, cantidad + 1):
    while True:
        try: 
            codigo = int(input(f'Ingrese codigo {i}:  '))
            if codigo > 10:
                break
            else: 
                print('Ingrese un codigo mayor a 10...')
        except:
            print('Ingrese solo numeros....')
        
        
    # contamos cuantos divisores tiene el numero (codigo)
    cantidad_resto_cero = 0
    
    for j in range(1, codigo + 1):
        if codigo % j == 0: # cuando codigo % j == 0, significa que j es divisor de codigo
            cantidad_resto_cero = cantidad_resto_cero + 1
        
            
            
        
    ## SI UN CODIGO TIENE 3 DIVISORES ES VALIDO 
    ## SI UN CODIGO TIENE 2 DIVISORERS ES PRIMO   
    if cantidad_resto_cero == 3:
        print('codigo valido')
        valido = valido + 1
    else:
        print('codigo INVALIDO')
        invalido = invalido + 1
        
# MOSTRAMOS LOS RESULTADOS:

print(f'\n Se ingresaron {valido} Codigos válidos..')
print(f'\n Se ingresaron {invalido} Codigos INVALIDOS...')
            
        


## 2

mayor = None
menor = None

# menu

while True:
    print('\n Registro de Temperatura..... ')
    print('1.- Ingresar Temp.')
    print('2- Mostrar Temp MAYOR.')
    print('3- Mostrar Temp MENOR.')
    print('4- Salir de programa.')
    
    opcion = input('Seleccione una opcion: ')
    
    if opcion == '1':
        while True:
            try:
                temp = int(input('Ingrese una temperatura entre -50 a 50: '))
                
                if  (temp < -50 or temp > 50):
                    print('Ingrese una temperatura entre -50 y 50..')
                else:
                    if mayor is None:
                        mayor = temp
                        menor = temp
                    else:
                        if temp > mayor:
                            mayor = temp
                        if  temp < menor:
                            menor = temp
                        print('Temperatura registrada......')
                        break                        
            except:
                print('Debe ingresar solo numeros...')                
            
    elif opcion == '2':
        if mayor == None:
            print('No se han registrado temperatura.... vaya a la opcion 1')
        else:
            print(f'La temperatura mayor es: {mayor}')
            
    elif opcion == '3':
        if menor == None:
            print('No se han registrado temperatura.... vaya a la opcion 1')
        else:
            print(f'La temperatura menor es: {menor}')        
        
    elif opcion == '4':
        print('Saliendo....')
        break
    else:
        print('Elija una opcion válida(1-4): ')

print('Fin del programa')
            
    



