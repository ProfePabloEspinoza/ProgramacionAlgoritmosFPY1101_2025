while True:
    try:
        cantidad = int(input("Ingrese la cantidad de libros prestados: "))
        break
    except:
        print("Debe ingresar un número entero.")

prestamos_largos = 0
prestamos_cortos = 0

for _ in range(cantidad):
    titulo = input("Ingrese el título del libro: ")
    
    while True:
        try:
            dias = int(input(f"Ingrese los días de préstamo para \"{titulo}\": "))
            break
        except:
            print("Debe ingresar un número entero.")
    
    if dias > 15:
        print("Préstamo por más de 15 días.")
        prestamos_largos += 1
    else:
        print("Préstamo por 15 días o menos.")
        prestamos_cortos += 1

print(f"\nSe registraron {prestamos_largos} libros con préstamo mayor a 15 días.")
print(f"Se registraron {prestamos_cortos} libros con préstamo de 15 días o menos.")
