arancel = 2200000
matricula = 95000

promedio = float(input("Ingrese su promedio: "))
decil = int(input("Ingrese el decil (1-10): "))

descuento_arancel = 0

if promedio > 6.5:
    if decil in [1, 2]:
        descuento_arancel = 0.25
    elif decil in [3, 4]:
        descuento_arancel = 0.18
elif 5.5 < promedio <= 6.5:
    if decil in [1, 2]:
        descuento_arancel = 0.15
    elif decil in [3, 4]:
        descuento_arancel = 0.12

precio_final_arancel = arancel * (1 - descuento_arancel)

descuento_matricula = 0

if decil in [1, 2, 3]:
    descuento_matricula = 0.12
    if promedio >= 6.0:
        descuento_matricula += 0.05

precio_final_matricula = matricula * (1 - descuento_matricula)

print(f"Arancel: ${precio_final_arancel:,.0f}")
print(f"Matrícula: ${precio_final_matricula:,.0f}")







rango_1 = int(input("ingrese un rango:"))
rango_2 = int(input("ingrese rango n:"))
if rango_1 >= rango_2:
    print("el primer valor debe ser menor que al segundo")
punto_medio = rango_1 + rango_2 / 2
ajuste = (rango_2 - rango_1) * 0.2

numero = int(random.choice(rango_1, rango_2))

numero_oculto = punto_medio + random.uniform(-ajuste, ajuste)
numero_oculto = round(numero_oculto)
intentos = []
for i in range ( 3):
    intento = int(input("intenta adivinar."))
    if intento == numero_secereto:
        print("felicidades adivinaste el numero")
    else:
        if i < 3 :
            pista = "mayor" if intento < numero_secereto else "menor"
            print(f"el numero de pista es {pista}.")
            if i == 2:
                de1 = intentos[1] - numero_secereto
                de2 = intentos[2] - numero_secereto
                cerca = intento [0] if de1 < de2 else intento[1]
                print(f"el numero es {cerca} que de {intentos[1]}")
        else:
            print("Perdiste")
            print(f"el numero era {numero_secereto}")