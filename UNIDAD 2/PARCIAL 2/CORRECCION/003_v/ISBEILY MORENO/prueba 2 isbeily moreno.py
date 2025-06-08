"""""
print ("calcularemos los beneficios a los estudiantes de primer año, segun sus condiciones academicas y socieconomicas")
promedio= float(input("ingresa tu promedio: "))
decil= float (input("ingresa tu decil (1/10): "))

arancel= 2200000
matricula= 95000
descuento_aracel= 0
descuento_matricula=0
descuento_por_promedio=0

if  promedio >= 6.5: 
  if  decil >= 1 and decil <= 2:
       descuento_aracel= 0.25
  else:
    descuento_aracel= 0.18
    
elif 5.5 <= promedio <= 6.5: 
   if decil >= 1 and decil <= 2:
      descuento_aracel = 0.15
   else:
    descuento_aracel= 0.12 
else:
     descuento_aracel= 0.0
      print ("no tienes descuento")

""""""

if decil >= 1 and 2 and decil <= 3:
 descuento_matricula= 0.12 

if promedio >= 6.0 and decil >= 1 and 2 and decil <= 3:
   descuento_por_promedio= 0.05


descuentos= ( arancel* descuento_aracel)
descuento_total= ( arancel - descuentos)

descuento_por_decil= (matricula * descuento_matricula)
descuento_total_decil= (matricula - descuento_por_decil)

descuento_promedio= (matricula * descuento_por_promedio)
descuento_total_promedio= (matricula - descuento_promedio)


print ("El valor del arancel con descuento es:", descuento_total)
print ("El valor de la matricula con descuento es:", descuento_por_decil)
print ("El descuento por promedio es:", descuento_total_promedio)

"""



import random

print("Hola, ingresa dos numeros y lo tienes que intentar adivinar")
num1 = int(input("Ingresa el primer número (numero menor): "))
num2 = int(input("Ingresa el segundo número (numero mayor): "))

if num1 >= num2:
    print("El primer número debe ser menor que el segundo. Por favor ingresa los números nuevamente")
else:
    punto_medio = (num1 + num2) / 2
    
    rango = num2 - num1
    ajuste = rango * 0.2
    
    numero_aleatorio = punto_medio + random.randint(-int(ajuste), int(ajuste))
    
    print("Bienvenido al juego, Tienes 3 intentos para adivinar el número")
    
    intentos = 0
    adivinado = False

    while intentos < 3 and not adivinado:
        intento_usuario = int(input(f"Intento {intentos + 1}: Adivina el número entre {num1} y {num2}: "))
        intentos += 1

        if intento_usuario == numero_aleatorio:
            print("felicitaciones, pudiste adivinar.")
            adivinado = True
        else:
            print(f"Perdiste :c ")
        
