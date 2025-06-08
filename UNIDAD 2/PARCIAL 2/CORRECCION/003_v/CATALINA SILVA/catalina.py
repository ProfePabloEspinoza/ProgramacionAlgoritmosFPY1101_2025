
promedio = float (input("ingrese su promedio: "))
decil = int (input("ingrese su decil: (1-4) "))

arancel_base = 2000200
matricula_base = 95.000

descuento_arancel = 0
descuento_matricula = 0 
descuento_promedio_extra = 0 # Nuevo descuento por promedio >= 6.0

if promedio >= 6.5: 
    if decil >= 1 and decil >= 2:
        descuento_arancel = 0.25
        descuento_matricula = 0.12
elif promedio >= 6.5: 
    if decil >= 3: 
        descuento_arancel = 0.18 
        descuento_matricula = 0.12
elif promedio >= 6.5:
    if decil >= 4: 
        descuento_arancel = 0.18 
        descuento_matricula = 0
elif 5.5 <= promedio < 6.5:
    if decil >= 1 and decil >= 2: 
        descuento_arancel = 0.15
        descuento_matricula = 0.12
elif 5.5 <= promedio < 6.5: 
    if decil >= 3:
        descuento_arancel = 0.12
        descuento_matricula = 0.12
elif 5.5 <= promedio < 6.5: 
    if decil >= 4: 
        descuento_arancel = 0.12
        descuento_matricula = 0

valor_arancel_final = arancel_base * (1 - descuento_arancel)
valor_matricula_final = matricula_base * (1 - descuento_matricula)
print (f"el valor total: {valor_arancel_final} - {valor_matricula_final}")


