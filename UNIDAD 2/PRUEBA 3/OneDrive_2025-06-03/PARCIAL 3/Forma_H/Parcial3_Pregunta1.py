while True:
    try:
        cant = int(input("Ingrese la cantidad de triángulos a calcular: "))
        if cant > 0:
            break
        else:
            print("Debe ingresar un número entero positivo.")
    except:
        print("Debe ingresar un número entero.")
suma_areas = 0.0
for i in range(cant):
    while True:
        try:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            if base > 0 and altura > 0:
                area = (base * altura) / 2
                print("Área:", area)
                suma_areas += area
                break
            else:
                print("Los valores deben ser positivos.")
        except:
            print("Debe ingresar valores numéricos válidos.")

print("Se calcularon", cant, "áreas de triángulos.")
print("La suma total de las áreas es:", suma_areas)
