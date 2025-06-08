promedio = float(input('Ingrese su promedio:'))
quintil = int(input('Ingrese el quintil (1,2,3,4 o 5):'))
descuento_A = 0
descuento_M = 0
    
if promedio > 6.0 and (quintil == 1 or quintil == 2):
  descuento_A = 0.2
elif promedio > 6.0 and (quintil == 3 or quintil == 4):
  descuento_A = 0.15
elif (promedio > 5.0 and promedio <= 6.0) and (quintil == 1 or quintil == 2):
  descuento_A = 0.13
elif (promedio > 5.0 and promedio <= 6.0) and (quintil == 3 or quintil == 4):
  descuento_A = 0.10
        
if quintil == 1 or quintil == 2 or quintil == 3:
  descuento_M = 0.1
  if promedio >= 5.5:
    descuento_M = 0.15
    
arancel = 1800000 - 1800000*descuento_A
matricula = 90000 - 90000*descuento_M
print('El valor del arancel es:', round(arancel))
print('El valor de la matricula es:', round(matricula))