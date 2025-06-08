meta_agua = 0.0
agua_bebida = 0.0
tengo_meta = False

# Mensaje de Bienvenida
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
        # Primero revisar si tengo meta establecida 
        if tengo_meta == False:
            print('Todavia no has establecido una meta, vaya primero a la opcion 1')
        else:
            print('\n ---- REGISTRAR AGUA BEBIDA ----')
            print('¿Cuanta agua quieres beber hoy?')
            print('Ejemplo: 2000 ml = 2 litros de agua = 8 vasos aprox.')

            # intentar leer un numero
            try:
                entrada = input('Escribe la cantidad de agua que bebí en ml: ')
                cantidad = float(entrada)

                # verificar que sea un numero positivo
                if cantidad <= 0:
                    print('La cantidad de agua debe ser mayor a cero')
                else:
                    # Sumando agua bebida a agua total
                    agua_bebida = agua_bebida + cantidad

                    print(f'Registrado: bebiste {cantidad} ml de agua hoy')
                    print(f'Total de agua bebida hoy: {agua_bebida} ml')

                    # dar un feedback de progreso
                    if agua_bebida >= meta_agua:
                        print('Felicidades, has alcanzado tu meta de agua')
                    else:
                        porcentaje = (agua_bebida / meta_agua) * 100
                        print(f'Progreso: {porcentaje:.0f}%')

            except ValueError:
                print('Error: debes ingresar numero')

    elif opcion == '3':
        print('\n ---- VER PROGRESO DETALLADO ----')

        if tengo_meta == False:
            print('Todavia no has establecido una meta, vaya primero a la opcion 1')
        else:
            print(f'Mi meta: {meta_agua} ml ')
            print(f'he bebido: {agua_bebida}')

            falta = meta_agua - agua_bebida
            print(f'Falta: {falta} ml')

            if agua_bebida >= meta_agua:

                extra = agua_bebida - meta_agua
                print(f'Extra: {extra} ml') 
                print(f'Felicidades, has alcanzado tu meta de agua, bebiste {extra} ml extra')
            else:
                print(f'No has alcanzado tu meta de agua, te falta {falta} ml')

                vasos = falta / 200 
                print(f'Te faltan {vasos} vasos de agua')
        
        input('\nPresiona enter para continuar.....')          

        
    elif opcion == '4':
        print('Nuevo dia iniciado....')

        confirmacion = input('Estas seguro? (s/n): ')
        if confirmacion.lower() == 's':
            meta_agua = 0.0
            agua_bebida = 0.0
            tengo_meta = False
        elif confirmacion.lower() == 'n':
            print('Cancelado. NO SE HA BORRADO NADA, QUEDATE TRANQUILO')
        else:
            print('debes elejir s o n')

    elif opcion == '5':
        print('Programa Terminado....')
        break

    else:
        print('\n Opcion no valida. Escriba un numero del 1 al 5')


# Fin de programa
print('Fin del Programa....')