#EJERCICO 1

print ("Hola, estudiante de primer año. Vamos a calcular tus beneficios según tus condiciones académicas y socioeconómcias")
condicion_academica = float(input("Por favor ingrese el promedio con que saliste del colegio/liceo (1.0 - 7.0) "))
condicion_socioeconomica = int(input("Ingresa el decil al que pertenece tu grupo familiar (1-10) "))

#Valores base
Arancel_base = 2200000
Matricula = 95000

#Cálculo beneficio arancel
if condicion_academica > 6.5 and (condicion_socioeconomica == 1 or condicion_socioeconomica == 2):
    print ("Usted tiene una bonificación del 25% de descuento en su arancel")
    bonificacion_arancel = 0.25 * Arancel_base

elif condicion_academica > 6.5 and (condicion_socioeconomica == 3 or condicion_socioeconomica == 4):
    print ("Usted tiene una bonificación del 18% de descuento en su arancel")
    bonificacion_arancel = 0.18 * Arancel_base

elif 5.5 < condicion_academica <= 6.5 and (condicion_socioeconomica == 1 or condicion_socioeconomica == 2):
    print ("Usted tiene una bonificación del 15% de descuento en su arancel")
    bonificacion_arancel = 0.15 * Arancel_base

elif 5.5 < condicion_academica <= 6.5 and (condicion_socioeconomica == 3 or condicion_socioeconomica == 4):
    print ("Usted tiene una bonificación del 12% de descuento en su arancel")
    bonificacion_arancel = 0.12 * Arancel_base

else:
    print("Usted no tiene ninguna bonificación en el arancel")
    bonificacion_arancel = 0.0

#Cálculo beneficio matricula
if condicion_socioeconomica == 1 or condicion_socioeconomica == 2 or condicion_socioeconomica == 3:
    print ("Usted tiene un descuento de 12% en su matrícula")
    bonificacion_matricula = 0.12 * Matricula
else:
    bonificacion_matricula = 0.0

#Cálculo beneficios adicionales
total_descuento_arancel = Arancel_base - bonificacion_arancel
print(total_descuento_arancel)
total_descuento_matricula = Matricula - bonificacion_matricula
print(total_descuento_matricula)

if (condicion_socioeconomica == 1 or condicion_socioeconomica == 2 or condicion_socioeconomica == 3) and condicion_academica >= 6.0:
    print("Usted obtiene un 5% adicional en ambos descuentos.")
    total_descuento_arancel_extra = (0.05 * total_descuento_arancel)
    total_descuento_matricula_extra = (0.05 * total_descuento_matricula)

total_final_arancel = total_descuento_arancel - total_descuento_arancel_extra
total_final_matricula = total_descuento_matricula - total_descuento_matricula_extra

print ("Por lo tanto. El monto total final de su arancel es de $", total_final_arancel, "y de su matrícula $", total_final_matricula)


#EJERCICIO 2

#Ingreso números
num1 = int(input("Ingresa el primer número (menor) "))
num2 = int(input("Ingresa el segundo número (mayor) "))

# Verificar que el primer número sea menor que el segundo
if num1 >= num2:
    print("El primer número debe ser menor que el segundo. Intenta de nuevo.")
else:
    #Punto medio
    punto_medio = (num1 + num2)/2
    #Ajuste 20%
    ajuste_20 = (num2 - num1) * 0.2

#Generar número aleatorio 
numero_aleatorio = int(punto_medio + ajuste_20)

#Juego
if num2 > num1:

    # Iniciar el contador de intentos
    intentos = 0
    acierto = False
    intentos_previos = []

    while intentos < 3:
        numero_ingresado = int(input(f"Intento {intentos+1} de 3: Intenta adivinar el número generado: "))
        intentos_previos.append(numero_ingresado)

        if numero_ingresado == numero_aleatorio:
            print("¡Felicitaciones, adivinaste el número!")
            acierto = True
            break
        else:
            if numero_ingresado < numero_aleatorio:
                print("El número es mayor.")
            else:
                print("El número es menor.")

     # Sugerencia después del segundo intento
        if intentos == 1 and (intentos_previos) == 2:
            distancia1 = abs(numero_aleatorio - intentos_previos[0])
            distancia2 = abs(numero_aleatorio - intentos_previos[1])
            if distancia1 < distancia2:
                print("El primer intento estuvo más cerca.")
            elif distancia2 < distancia1:
                print("El segundo intento estuvo más cerca.")
            else:
                print("Ambos intentos estuvieron igual de cerca.")

        intentos = intentos + 1

    if not acierto:
        print(f"No lograste adivinar el número. Era: {numero_aleatorio}")