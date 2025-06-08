
meta_agua = 0.0
agua_bebida = 0.0
tengo_meta = False


print('!Control de hidratación!')
print('Los adultos deben beber entre 2 - 3 litros de agual (2000 - 3000 ml)')


while True:
    # Mostrar Información Actual

    print('\n' + '-'*50)
    print('ESTADO ACTUAL: ')

    if tengo_meta == True:
        print(f'Mi meta: {meta_agua} ml ')
        print(f'he bebido: {agua_bebida}')

        # Calcular y mostrar porcentaje 
        porcentaje = (agua_bebida / meta_agua) * 100
        print(f'Progreso: {porcentaje:.0f}%')
    else:
        print('Todavia no has establecido una meta')
    
    # Mostrar el Menú:
    print('\n¿Que quieres hacer?')
    print('1.- Establecer mi meta de agua para hoy')
    print('2.- Registrar agua que bebí')
    print('3.- Ver mi progreso detallado')
    print('4.- Empezar un nuevo dia (borrar todo)')
    print('5.- Salir del programa')
    print('-'*50)

    # pedir opcion al usuario

    opcion = input('Elija una opcion (1-5): ')

    if opcion == '1':
        
        print('\n ---- ESTABLECER META DIARIA ----')
        print('¿Cuanta agua quieres beber hoy?')
        print('Ejemplo: 2000 ml = 2 litros de agua = 8 vasos aprox.') 

        # intentar leer un numero
        try:
            entrada = input('Escribe tu meta en ml: ')
            meta_agua = float(entrada)

            # verificar que sea un numero positivo
            if meta_agua <= 0:
                print('La meta meta debe ser mayor a cero')
            else:
                tengo_meta = True
                print(f'Perfecto: tu meta es beber {meta_agua} ml hoy')
        except ValueError:
            print('Error: debes ingresar numero')




    elif opcion == '2':
        pass
    elif opcion == '3':
        pass
    elif opcion == '4':
        pass
    elif opcion == '5':

        print('\n Hasta luego! Recuerda mantenerte hidratado...')
        break
    
    else:
        print('\n Opcion no valida. Escriba un numero del 1 al 5')

# Fin de programa
print('Programa Terminado....')


