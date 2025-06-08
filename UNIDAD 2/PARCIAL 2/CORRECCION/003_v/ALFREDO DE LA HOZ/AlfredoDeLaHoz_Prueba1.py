#Prueba Alfredo De La Hoz
#Se ingresan los datos y valores
matricula = 95000
arancel = 2200000
promedio = float(input("Ingrese su promedio NEM: "))
rsh = int(input("Ingrese su decil (1-10): "))

#Se calcula el arancel según los datos recibidos
if promedio > 6.5 and (rsh == 1 or rsh == 2):
    dcto_arancel = 0.25
elif promedio > 6.5 and (rsh == 3 or rsh == 4 ):
    dcto_arancel = 0.18  
elif promedio > 5.5 and promedio <= 6.5 and (rsh == 1 or rsh == 2):
    dcto_arancel = 0.15
elif promedio > 5.5 and promedio <= 6.5 and (rsh == 3 or rsh == 4):
    dcto_arancel = 0.12
else:
    dcto_arancel = 0.0    

#se calcula la matricula segun los datos recibidos
dcto_matricula = (float(0.0)) 
if rsh == 1 or rsh == 2 or rsh == 3:
    dcto_matricula = (float(0.12))
    if promedio >= 6.0:
        dcto_matricula += (float(0.05))

#se aplica la formula para los descuentos
desc_arancel = int(arancel - (arancel * dcto_arancel))
desc_matricula = int(matricula - (matricula * dcto_matricula))

#se imprime
print(f"Usted por tener promedio de {promedio} y por pertenecer al decil {rsh}, obtiene los siguientes valores respecto a precios:\nMatricula: {desc_matricula}$\nArancel: {desc_arancel}$")
if promedio >= 5.5 or rsh == 1 or rsh == 2 or rsh == 3 or rsh == 4:
    print("Obtuviste uno o mas descuentos debido a tu promedio/condicion socioeconomica.")