#10/05/2025
#Ghislaine Carrasco. FPY1101. 

arancel = 2200000
matricula = 95000
promedio =float(input("Ingrese su promedio final de colegio o liceo: "))
decil = int(input("Ingrese el decil (1-4): "))
valor_arancel = 0 ; valor_matricula = 0
descuento_matricula = 0.0 ; valor_final_matricula = 0


if promedio > 6.5:
    if (decil == 1) or (decil == 2):
        descuento_arancel = 0.25
        valor_arancel = arancel * (1 - descuento_arancel)
elif promedio > 6.5:
    if (decil == 3) or (decil == 4):
        descuento_arancel = 0.18
        valor_arancel = arancel * (1 - descuento_arancel)
elif promedio <= 5.5 and promedio <= 6.5:
    if (decil == 1) or (decil == 2):
        descuento_arancel = 0.15
        valor_arancel = arancel * (1 - descuento_arancel)
elif promedio <= 5.5 and promedio <= 6.5:
    if (decil == 3) or (decil == 4):
        descuento_arancel = 0.12
        valor_arancel = arancel * (1 - descuento_arancel)
else: 
    print(" ")

if promedio >= 6.0:
    if (decil == 1) or (decil == 2) or (decil == 3):
        descuento_matricula = 0.12
        valor_desc_matricula = matricula * (1 - descuento_matricula)
        descuento_adicional = 0.05
        valor_final_matricula = valor_desc_matricula * (1 - descuento_adicional)
    print("Usted no tiene descuento en la matricula.")


    
    

print("Valor Arancel:", arancel)
print("Valor Matricula:", matricula)
print("Valor final arancel:", valor_arancel)
print("Valor final de matricula:", valor_final_matricula)




