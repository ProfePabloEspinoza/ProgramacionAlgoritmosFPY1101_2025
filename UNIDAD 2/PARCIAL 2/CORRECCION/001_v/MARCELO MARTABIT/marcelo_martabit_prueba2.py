promedio = float(input("Ingrese su promedio: "))
decil = int(input("Ingrese su decil (1-10): "))

arancel_base = 2200000
matricula_base = 95000

if promedio > 6.5:
    if 1 <= decil <= 2:
        desc_ara = 0.25
    elif 3 <= decil <= 4:
        desc_ara = 0.18
    else:
        desc_ara = 0
elif 5.5 <= promedio <= 6.5:
    if 1 <= decil <= 2:
        desc_ara = 0.15
    elif 3 <= decil <= 4:
        desc_ara = 0.12
    else:
        desc_ara = 0
else:
    desc_ara = 0

if 1 <= decil <= 3:
    desc_mat = 0.12
    if promedio >= 6.0:
        desc_mat += 0.05
else:
    desc_mat = 0

arancel_final = int(arancel_base * (1 - desc_ara))
matricula_final = int(matricula_base * (1 - desc_mat))

print(f"El valor del arancel es: {arancel_final}")
print(f"El valor de la matricula es: {matricula_final}")


# --------------------------


num1 = int(input("Ingrese limite inferior: "))
num2 = int(input("Ingrese limite superior: "))

punto_medio = (num1 + num2) / 2
ajuste = (num2-num1) * 0.2

# Test
#print("punto medio",punto_medio)
#print("ajuste",ajuste)

rango_bajo = int(punto_medio-ajuste)
rango_alto = int(punto_medio+ajuste)

# Test
#print("rango bajo",rango_bajo)
#print("rango alto",rango_alto)

import random
random = random.randint(rango_bajo,rango_alto)
# Test
#print("random",random)

if num1 > num2:
    print("El limite inferior debe ser menor al limite superior")
elif num1 == num2:
    print("Los limites no pueden ser iguales")
else:
    #intento 1
    intento1 = int(input("Intente adivinar: "))
    if intento1 == random:
        print("Felicitaciones, pudiste adivinar")
    elif intento1 > random:
        print("El numero es menor")
        #intento 2
        intento2 = int(input("Intente adivinar: "))
        if intento2 == random:
            print("Felicitaciones, pudiste adivinar")
        elif intento2 > random:
            print("El numero es menor")
            # pista
            if abs(random - intento1) < abs(random - intento2):
                print(f"El numero que buscas esta mas cerca de {intento1} que de {intento2}")
            elif abs(random - intento2) < abs(random - intento1):
                print(f"El numero que buscas esta mas cerca de {intento2} que de {intento1}")
            elif abs(random - intento1) == abs(random - intento2):
                print("Ambos numero estan igual de cerca")
            # intento 3
            intento3 = int(input("Intente adivinar: "))
            if intento3 == random:
                print("Felicitaciones, pudiste adivinar")
            else:
                print("Perdiste")
                print(f"El numero era {random}")
            # -------------
        elif intento2 < random:
            print("El numero es mayor")
            # pista
            if abs(random - intento1) < abs(random - intento2):
                print(f"El numero que buscas esta mas cerca de {intento1} que de {intento2}")
            elif abs(random - intento2) < abs(random - intento1):
                print(f"El numero que buscas esta mas cerca de {intento2} que de {intento1}")
            elif abs(random - intento1) == abs(random - intento2):
                print("Ambos numero estan igual de cerca")
            # intento 3
            intento3 = int(input("Intente adivinar: "))
            if intento3 == random:
                print("Felicitaciones, pudiste adivinar")
            else:
                print("Perdiste")
                print(f"El numero era {random}")
            # ---------------------
    # intento 1
    elif intento1 < random:
        print("El numero es mayor")
        # intento 2
        intento2 = int(input("Intente adivinar: "))
        if intento2 == random:
            print("Felicitaciones, pudiste adivinar")
        elif intento2 > random:
            print("El numero es menor")
            # pista
            if abs(random - intento1) < abs(random - intento2):
                print(f"El numero que buscas esta mas cerca de {intento1} que de {intento2}")
            elif abs(random - intento2) < abs(random - intento1):
                print(f"El numero que buscas esta mas cerca de {intento2} que de {intento1}")
            elif abs(random - intento1) == abs(random - intento2):
                print("Ambos numero estan igual de cerca")
            # intento 3
            intento3 = int(input("Intente adivinar: "))
            if intento3 == random:
                print("Felicitaciones, pudiste adivinar")
            else:
                print("Perdiste")
                print(f"El numero era {random}")
            # -------------
        elif intento2 < random:
            print("El numero es mayor")
            # pista
            if abs(random - intento1) < abs(random - intento2):
                print(f"El numero que buscas esta mas cerca de {intento1} que de {intento2}")
            elif abs(random - intento2) < abs(random - intento1):
                print(f"El numero que buscas esta mas cerca de {intento2} que de {intento1}")
            elif abs(random - intento1) == abs(random - intento2):
                print("Ambos numero estan igual de cerca")
            # intento 3
            intento3 = int(input("Intente adivinar: "))
            if intento3 == random:
                print("Felicitaciones, pudiste adivinar")
            else:
                print("Perdiste")
                print(f"El numero era {random}")
            # ---------------------


