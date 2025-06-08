#Ejercicio 1
"""
# Estare atenta a su feedback

print("¡Hola! Para saber tu descuentos de Matricula y Arancel por favor ingresa los siguientes datos:  ")
promedio = float(input("ingrese su promedio final: "))
decil = int(input("Ingrese su decil 1-10: "))

descuento = 0
descuento_promedio = 0
descuento_decil = 0
arancel = 2200000
matricula = 95000
descuento_total = 0

if promedio > 6.5:
    if decil == 1 or decil == 2:
        descuento_decil = 0.25 
    elif decil == 3 or decil == 4:
        descuento_decil = 0.18    
elif 5.5 < promedio <= 6.5:
    if decil == 1 or decil == 2:
        descuento_decil = 0.15
    elif decil == 3 or decil == 4:
        descuento_decil = 0.12
else: 
    descuento_decil = 0

if promedio >=  6.0:
    descuento_promedio = 0.05

if decil == 1 or decil == 2 or decil == 3:
    descuento = 0.12    
 

 

descuento_total = descuento_decil + descuento_promedio + descuento


preciofinal_arancel = (arancel * ( 1- descuento_total))

preciofinal_matricula = (matricula * ( 1 - descuento_total)) 

print("Se han aplicado los descuentos, los valores a cancelar son los siguientes: ")
print(f"Valor Arancel: $", round (preciofinal_arancel) )
print(f"Valor Matricula: $", round (preciofinal_matricula) )

"""
# Ejercicio 2
"""

#Profe disculpe aca no entendi nada, de igual manera quedo atenta al feedback!
num1 = int(input("ingrese un primer numero (Debe ser menor al primero): "))
num2 = int(input("Ingrese un segundo numero (Debe ser mayor al primero): "))

punto_medio=num1+num2 / 2



print(punto_medio)
"""