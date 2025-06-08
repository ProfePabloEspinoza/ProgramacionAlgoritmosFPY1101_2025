print("Bienvenido a su sistema de calculo de becas, el arancel es de $2200000 y la matricula es de $95000")
promedio=float(input("Ingrese su promedio: [recureda ingresar los numeros con punto]"))
decil=int(input("Ingrese su decil: "))
matricula=95000
arancel_base=2200000
descuento=0.0
matricula_final=0.0
matricula_final=0.0
if    promedio> 6.5 and decil in [1,2]:
        descuento=0.25
elif promedio>6.5 and decil in [3,4]:
        descuento=0.18
elif 5.5<promedio<=6.5 and decil in [1,2]:
        descuento=0.15
elif 5.5<promedio<=6.5 and decil in [3,4]:
        descuento=0.12
else:
        descuento=0
arancel_final1 = int(arancel_base*(1-descuento))
if decil in [1,2,3] and promedio>=6.0:
        arancel_final1=arancel_final1*(1-0.05)
        matricula_final=matricula*(1-0.12)
elif decil in [1,2,3]:
        matricula_final=matricula*(1-0.12)

print(f"El valor de su matricula es {matricula_final} y su arancel es {arancel_final1} ")