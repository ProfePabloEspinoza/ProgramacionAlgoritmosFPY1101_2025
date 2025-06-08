#PRIMER EJERCICIO: 
arancel = 2200000
matricula = 95000

promedio = float(input("Ingrese su promedio: "))
decil = int(input("Ingrese el decil (1-10): "))

if 6.5 < promedio <= 7.0:
    if decil == 1 or decil == 2:
        total = arancel * 0.75
    elif decil == 3 or decil == 4:
        total = arancel * 0.82
    elif decil < 0: print("El decil no puede ser menor a 1, inténtelo de nuevo")
    elif decil > 10: print("El decil no puede ser mayor a 10, inténtelo de nuevo")
    else: print("Ingrese valores númericos, inténtelo de nuevo")
elif 5.5 < promedio <= 6.5:
    if decil == 1 or decil == 2:
        total = arancel * 0.85
    elif decil == 3 or decil == 4:
        total = arancel * 0.88
    elif decil < 0: print("El decil no puede ser menor a 1, inténtelo de nuevo")
    elif decil > 10: print("El decil no puede ser mayor a 10, inténtelo de nuevo")
    else: print("Ingrese valores númericos, inténtelo de nuevo")
elif 0 < promedio <= 5.5: total = arancel
else: print("El promedio no es correcto, inténtelo de nuevo")

if decil == 1 or decil == 2 or decil == 3:
    if 6.0 <= promedio <= 7.0:
        matricula *= 0.83
    elif 1.0 <= promedio < 6.0:
        matricula *= 0.88
else: matricula = matricula
#En el ejemplo 1 del enunciado de la prueba 
#Se indica que el resultado debe ser matrícula = 78.375
#Cosa que es errónea
print(f"El valor del arancel es: {total}" "\n" f"El valor de la matrícula es: {matricula}")

#SEGUNDO EJERCICIO:
#Decidí no usar un búcle porque no entra dentro del contenido dado hasta la fecha 
print("Bienvenido al juego de adivinar el número aleatorio" "\n" "Debes adivinar el número final" "\n")
print("El PRIMER número debe ser MENOR que el SEGUNDO" "\n")
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

if num1 > num2:
    print("El primer número debe ser menor que el segundo")
elif num1 < num2:
    punto_medio = (num1 + num2) / 2
    ajuste = (num2 - num1) * 0.2
    num_adivinar = punto_medio + ajuste #En el enunciado se indica que puede ser suma o resta

print("Información:")
print(f"El primer número es {num1}" "\n" f"El segundo número es {num2}")
print("Tienes solo 3 intentos para lograr adivinarlo")
print(" ")

primer_intento = int(input("Ingresa tu primer intento: "))

if primer_intento == num_adivinar: print("Felicitaciones, pudiste adivinar")
elif primer_intento < num_adivinar: print(f"Estás cerca, pero es un monto MAYOR que {primer_intento}")
elif primer_intento > num_adivinar: print(f"Estás cerca, pero es un monto MENOR que {primer_intento}")
else: print("Entrada inválida")

print(" ")

segundo_intento = int(input("Ingresa tu segundo intento: "))
if segundo_intento == num_adivinar: print("Felicitaciones, pudiste adivinar")
elif segundo_intento < num_adivinar: print(f"Estás cerca, pero es un monto MAYOR que {segundo_intento}")
elif segundo_intento > num_adivinar: print(f"Estás cerca, pero es un monto MENOR que {segundo_intento}")
else: print("Entrada inválida")

if primer_intento > num_adivinar:
    cerca1 = primer_intento - num_adivinar
elif primer_intento < num_adivinar:
    cerca1 = num_adivinar - primer_intento

if segundo_intento > num_adivinar:
    cerca2 = segundo_intento - num_adivinar
elif segundo_intento < num_adivinar:
    cerca2 = num_adivinar - segundo_intento

print(" " "\n" "Acá una pista que te puede ayudar ;)")
if cerca1 < cerca2: print(f"El PRIMER intento ({primer_intento}) estuvo más cerca que el segundo ({segundo_intento})")
elif cerca1 > cerca2: print(f"El SEGUNDO intento ({segundo_intento}) estuvo más cerca que el primero ({primer_intento})")
elif cerca1 == cerca2: print("Ambos intentos estuvieron igual de cerca" "\n" f"Primer intento {primer_intento}" "\n" f"Segundo intento {segundo_intento}")

print(" ")

tercer_intento = int(input("Ingresa tu tercer y último intento: "))
if tercer_intento == num_adivinar: print("Felicitaciones, pudiste adivinar")
else: print(f"Perdiste :( el arancel final era {num_adivinar}")
#recordar que hay un error en llos resultados indicados en el enunciado