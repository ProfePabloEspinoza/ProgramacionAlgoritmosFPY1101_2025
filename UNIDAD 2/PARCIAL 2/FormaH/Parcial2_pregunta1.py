# Solicitar datos al usuario
quintil = int(input("Ingrese su quintil (1-5): "))
condicion = input("Ingrese su condición laboral (empleado/desempleado): ").strip().lower()
edad = int(input("Ingrese su edad: "))

# Determinar el subsidio base según quintil y condición laboral
if quintil in [1, 2]:
    subsidio = 10000 if condicion == "desempleado" else 8000
elif quintil == 3:
    subsidio = 6000 if condicion == "desempleado" else 4000
elif quintil in [4, 5]:
    subsidio = 1500
else:
    subsidio = 0  # Si el quintil ingresado es inválido

# Aplicar bonos adicionales
if quintil in [1, 2]:
    subsidio += 2000
if quintil in [1, 2] and edad > 65:
    subsidio += 3000

# Mostrar resultado
print(f"El valor del subsidio de gas es: ${subsidio:,}".replace(",", "."))



