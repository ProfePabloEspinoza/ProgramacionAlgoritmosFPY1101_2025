# Ejercicio Número 1 

"""
print( '+' + '-' * 35 + '+')
print("         Beneficios estudiantiles")
print( '+' + '-' * 35 + '+')

print(" El programa le ayudará a calcular los beneficios estudiantiles de 1er año basado en sus condiciones académicas y socioeconómicas.")

promedio_media= float(input("Ingrese el promedio final de la media: "))
cond_socioeconmica= int(input(" Ingrece el decil al que pertenece su gripo familiar: \n (1 - 10): "))

beneficio = 0

arancel= 2200000
matricula= 95000

if promedio_media >6.5:
    if cond_socioeconmica == 1 or cond_socioeconmica == 2:
        beneficio = 0.25
    else: 
        beneficio = 0.18
elif 5.5 < promedio_media <= 6.5:
    if cond_socioeconmica == 1 or cond_socioeconmica == 2:
        beneficio = 0.15
    else:
        beneficio = 0.12

if cond_socioeconmica == 1 or cond_socioeconmica == 2 or cond_socioeconmica == 3:
    descuento_matricula = 0.12
    if promedio_media >= 6.0:
        descuento_matricula += 0.05
else:
    descuento_matricula = 0

arancel_final = int(arancel * (1 - beneficio))
matricula_final = int(matricula * (1 - descuento_matricula))

print(" El valor del arancel es:", arancel_final)
print(" El valor de la matricula es de:", matricula_final)

"""
#Ejercicio Número 2

num1 = int(input("Ingrese el número inferior: "))
num2 = int(input("Ingrese el número superior: "))

if num1 < num2:
    if (num2 - num1) % 10 == 0:
        numero_objetivo = num2
    else:
        numero_objetivo = int((num1 + num2) / 2)

    
    intento1 = int(input("Intente adivinar: "))
    if intento1 == numero_objetivo:
        print("Felicitaciones, adivinó en su primer intento.")
    else:
        if intento1 < numero_objetivo:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        
        intento2 = int(input("Intente de nuevo: "))
        if intento2 == numero_objetivo:
            print("Felicitaciones, adivinó en su segundo intento.")
        else:
            if intento2 < numero_objetivo:
                print("El número es mayor.")
            else:
                print("El número es menor.")

            print("Te daré una pista:")

            diferencia1 = abs(numero_objetivo - intento1)
            diferencia2 = abs(numero_objetivo - intento2)

            if diferencia1 < diferencia2:
                print("El número que buscas está más cerca de", intento1, "que de", intento2)
            elif diferencia2 < diferencia1:
                print("El número que buscas está más cerca de", intento2, "que de", intento1)
            else:
                print("Ambos intentos estuvieron igual de cerca.")

          
            intento3 = int(input("Intente la última vez: "))
            if intento3 == numero_objetivo:
                print("Felicitaciones, adivinó en su tercer intento.")
            else:
                print("Perdiste.")
                print("El número era:", numero_objetivo)
else:
    print("Error: el límite inferior debe ser menor que el límite superior.")
