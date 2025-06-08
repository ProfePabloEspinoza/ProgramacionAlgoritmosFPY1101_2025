
"""""
arancel = 2200000
matricula = 95000

promedio = float(input("Ingrese su promedio: "))
decil = int(input("Ingrese su decil: (1-10) "))

if (promedio >= 6.0) and (1 <= decil <= 3):
 descuentoarancel = (arancel * 25) / 100
 descuentomatricula = (matricula * 17) / 100  
 matricula = matricula - descuentomatricula
elif (promedio > 6.5) and (1 <= decil <= 2):
 descuentoarancel = (arancel * 25) / 100
elif (promedio > 6.5) and (3 <= decil <= 4):
 descuentoarancel = (arancel * 18) / 100
elif (5.5 <= promedio <= 6.5) and (1 <= decil <= 2):
 descuentoarancel = (arancel * 15) / 100
elif (5.5 <= promedio <= 6.5) and (3 <= decil <= 4):
 descuentoarancel = (arancel * 12) / 100

print(f"\n El valor de la matricula es: {matricula}")
print(f"El valor del arancel es: {arancel - descuentoarancel}

"""

num1 = int(input("Ingrese el límite inferior: "))
num2 = int(input("Ingrese el límite superior: "))

puntomedio = num1+num2 / 2 

ajuste = (num2-num1) * 0.2

numerogenerado = ajuste + puntomedio


respuesta = int(input("Adivine el número: "))
while respuesta != numerogenerado:
    if respuesta > numerogenerado:
     print("El número es menor.") 
    else:
     print("El número es mayor")


             
