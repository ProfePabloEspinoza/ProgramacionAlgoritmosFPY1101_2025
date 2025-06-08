#ejercicio 1 

matricula = 95000
arancel = 2200000

promedio = float(input("Ingrese su promedio: "))
decil = int(input("Ingrese su decil: "))
    
    
if promedio < 0 or promedio > 7:
        print("Error: El promedio debe estar entre 0 y 7.")
elif decil < 1 or decil > 10:
        print("Error: El decil debe estar entre 1 y 10.")
else:
    descuento_arancel = 0.0
    descuento_matricula = 0.0
        
       
    if promedio > 6.5 and (decil == 1 or decil == 2):
            descuento_arancel = 0.25  
    elif promedio > 6.5 and (decil == 3 or decil == 4):
            descuento_arancel = 0.18  
    elif promedio > 5.5 and promedio <= 6.5 and (decil == 1 or decil == 2):
            descuento_arancel = 0.15  
    elif promedio > 5.5 and promedio <= 6.5 and (decil == 3 or decil == 4):
            descuento_arancel = 0.12  
        
   
    if decil == 1 or decil == 2 or decil == 3:
            descuento_matricula = 0.12 
    if promedio >= 6.0:
                descuento_matricula = 0.12 + 0.05  
        
   
    valor_arancel = arancel * (1 - descuento_arancel)
    valor_matricula = matricula * (1 - descuento_matricula)
        
    
    print("Valor del arancel: ", int(valor_arancel))
    print("Valor de la matrícula: ", int(valor_matricula))



#ejercicio 2 

num1 = 1
num2 = 10
    

punto_medio = (num1 + num2) / 2  
    
 
ajuste = (num2 - num1) * 0.2  
    
    
numero_generado = int(punto_medio + ajuste)  
    
   
if numero_generado < num1:
        numero_generado = num1
elif numero_generado > num2:
        numero_generado = num2
    
    
print("¡Bienvenido al juego!")
print(f"Intenta adivinar un número entre {num1} y {num2}. Tienes 3 intentos.")
    
   
adivinanza1 = int(input("Primer intento: "))
if adivinanza1 == numero_generado:
        print("Felicitaciones, pudiste adivinar")
else:
    if adivinanza1 < numero_generado:
            print("El número es mayor.")
    else:
            print("El número es menor.")
        
    adivinanza2 = int(input("Segundo intento: "))
    if adivinanza2 == numero_generado:
            print("Felicitaciones, pudiste adivinar")
    else:
        if adivinanza2 < numero_generado:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    diferencia1 = abs(adivinanza1 - numero_generado)
    diferencia2 = abs(adivinanza2 - numero_generado)

if diferencia1 < diferencia2:
    print(f"Pista: Tu primer intento ({adivinanza1}) estuvo más cerca que el segundo ({adivinanza2}).")
elif diferencia2 < diferencia1:
    print(f"Pista: Tu segundo intento ({adivinanza2}) estuvo más cerca que el primero ({adivinanza1}).")
else:
    print("Pista: Ambos intentos estuvieron cerca misma del número.")
            
         
adivinanza3 = int(input("Tercer intento: "))
if adivinanza3 == numero_generado:
    print("Felicitaciones, pudiste adivinar")
else:
    print("Perdiste. El número era:", numero_generado)
