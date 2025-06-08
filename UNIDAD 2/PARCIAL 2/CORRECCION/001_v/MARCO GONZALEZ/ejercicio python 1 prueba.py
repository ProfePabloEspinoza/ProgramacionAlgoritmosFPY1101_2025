

arancel = 2200000 
mensualidad = 95000
descuento_arancel = 0
descuento_mensualidad = 0
promedio = float(input("ingrese su promedio: "))
decil = int(input("ingrese su decil (1-10): "))

if promedio > 6.5:
  if decil == 1 or decil == 2:
    descuento_arancel = 0.25
  elif decil == 3 or decil == 4:
    descuento_arancel = 0.18
elif promedio > 5.5:
  if decil == 1 or decil == 2:
    descuento_arancel = 0.15
elif decil == 3 or decil == 4:
  descuento_arancel == 0.12 

valor_arancel = arancel * (1-descuento_arancel)


if decil == 1 or decil == 2 or decil == 3:
  descuento_mensualidad = 0.12
  if promedio >= 6.0:
   descuento_mensualidad += 0.05


valor_mensualidad = mensualidad * (1-descuento_mensualidad)

print(f"el valor de su arancel es: {int(valor_arancel)} " )
print(f"el valor de su mensualidad es: {int(valor_mensualidad)} ")