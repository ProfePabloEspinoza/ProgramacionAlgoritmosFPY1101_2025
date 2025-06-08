while True:
    try:
        cant = int(input("Ingrese la cantidad de personas a registrar: "))
        break
    except:
        print("Debe ingresar un número entero.")

esquema_completo = 0
esquema_incompleto = 0
dosis_completas = 3  # Definir la cantidad de dosis necesarias para esquema completo

for _ in range(cant):
    while True:
        try:
            dosis = int(input("Ingrese cantidad de dosis recibidas: "))
            break
        except:
            print("Debe ingresar un número entero.")
    if dosis >= dosis_completas:
        print("Esquema completo.")
        esquema_completo += 1
    else:
        print("Esquema incompleto.")
        esquema_incompleto += 1

print(f"Se registraron {esquema_completo} personas con esquema completo.")
print(f"Se registraron {esquema_incompleto} personas con esquema incompleto.")
