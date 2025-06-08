user1 = ''
user2 = ''
user3 = ''
edad1 = 0
edad2 = 0
edad3 = 0
flag = True
while flag:
    print("1.- Ingresar usuario y contraseña.\n2.- Calcular edad promedio.\n3.- Salir.")
    op1 = input('Seleccione opción: ')

    if op1 == '1':
        nombre = input('Ingrese nombre de usuario: ')
        while True:
            edad = input('Ingrese edad del usuario: ')
            try:
                edad = int(edad)
                break
            except:
                print("Debe ingresar la edad como numero entero.\n Intentelo nuevamente.")
        if user1 == '':
            user1 = nombre
            edad1 = edad
        elif user2 == '':
            user2 = nombre
            edad2 = edad
        elif user3 == '':
            user3 = nombre
            edad3 = edad
        else:
            print('No se pueden ingresar más usuarios.')
      
    elif op1 == '2':
        n = 0
        if edad1 != 0:
            n+=1
        if edad2 != 0:
            n+=1
        if edad3 != 0:
            n+=1  
        if n==1:
            promedio = round((edad1)/n,1)
        elif n==2:
            promedio = round((edad1+edad2)/n,1)
        elif n==3:
            promedio = round((edad1+edad2+edad3)/n,1)
        if n!=0:
            print("La edad promedio de los usuarios es:", promedio)
        else:
            print("No es posible calcular promedio.")  
            
    elif op1 == '3':
        flag = False
    else: 
        print("Seleccione una opción valida.")