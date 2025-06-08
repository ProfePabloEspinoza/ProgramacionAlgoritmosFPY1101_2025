print()
print(":::::::::Beneficios Arancelarios::::::::")
print()
print("Calcula tu descuento en el arancel y matricula")
print()



promedio_estudiante= int(input("Ingrese su promedio:"))
decil_socioeconomico= int(input("ingrese su decil socioeconomico (1-10):"))
valor_arancel= int(input("Ingrese el valor del arancel:"))
valor_matricula=int(input("Ingrese el valor de la matricula:"))


descuento_arancel=0
niveles_decil=[1,2,3,4,5,6,7,8,9,10]

# Solicitar el promedio del estudiante
if promedio_estudiante > 6.5 and decil_socioeconomico  in [1,2]:
     descuento_arancel=0.25
elif  promedio_estudiante > 6.5 and decil_socioeconomico in [3,4]:
     descuento_arancel=0.18
elif 5.5 < promedio_estudiante <= 6.5 and decil_socioeconomico in [1,2]:
     descuento_arancel=0.15
elif 5.5 < promedio_estudiante <= 6.5 and decil_socioeconomico in [3,4]:
     descuento_arancel=0.12
else:
        descuento_arancel=0.0
        print("No tienes descuentos adicionales")

if decil_socioeconomico in [1,2,3]:
     descuento_arancel +=0.12

if decil_socioeconomico in [1,2,3] and promedio_estudiante >= 6.0:
     descuento_arancel +=0.05
else:
     descuento_arancel=0.0
     print("No tienes descuentos adicionales")

# Calcular el valor del arancel con descuento
valor_arancel_descuentos= valor_arancel * (1 - descuento_arancel)

print()
print("::::::::Detalle de tu matricula:::::::::")
print()
print(f"El total de tu descuento es: {descuento_arancel*100:.0f}%")
print(f"El valor del arancel con descuento es:{valor_arancel_descuentos:.0f}")
print(f"El valor de tu matricula es: {valor_matricula:.0f}")
print(f"El total a cancelar es: {valor_arancel_descuentos + valor_matricula:.0f}")






