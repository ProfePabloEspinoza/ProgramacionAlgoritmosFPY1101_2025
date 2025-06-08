# Solicitar datos al usuario
quintil = int(input("Ingrese su quintil (1-5): "))
condicion = input("Ingrese su condición laboral (empleado/desempleado): ").strip().lower()
edad = int(input("Ingrese su edad: "))

# Determinar el subsidio base según quintil y condición laboral
if quintil in [1, 2]:
    subsidio = 350000 if condicion == "desempleado" else 280000
elif quintil == 3:
    subsidio = 250000 if condicion == "desempleado" else 200000
else:
    subsidio = 0  # No hay subsidio para quintiles 4 y 5

# Aplicar bonos adicionales
if quintil in [1, 2]:
    subsidio += 60000
if quintil in [1, 2] and edad > 65:
    subsidio += 40000

# Mostrar resultado
print(f"El valor del subsidio de arriendo es: {subsidio:,}".replace(",", "."))
