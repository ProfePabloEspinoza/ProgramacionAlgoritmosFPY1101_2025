while True:
    try:
        cant = int(input("Ingrese la cantidad de empleados a registrar: "))
        break
    except:
        print("Debe ingresar un número entero.")

mas_de_10 = 0
menos_o_igual_10 = 0

for _ in range(cant):
    nombre = input("Ingrese nombre del empleado: ")
    
    valido = False
    while not valido:
        try:
            anios = int(input("Ingrese años de antigüedad: "))
            valido = True
        except:
            print("Debe ingresar un número entero.")
    
    if anios > 10:
        print("Más de 10 años de antigüedad.")
        mas_de_10 += 1
    else:
        print("10 o menos años de antigüedad.")
        menos_o_igual_10 += 1

print(f"\nSe registraron {mas_de_10} empleados con más de 10 años de antigüedad.")
print(f"Se registraron {menos_o_igual_10} empleados con 10 o menos años de antigüedad.")
