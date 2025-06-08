quintil = int(input('Ingrese su quintil (1-5): '))
condicion_laboral = input('Ingrese su condición laboral (empleado/desempleado): ').strip().lower()
edad = int(input('Ingrese su edad: '))

subsidio = 0
bono_adicional = 0

# Definir subsidio según quintil y condición laboral
if quintil in [1, 2]:
    if condicion_laboral == "desempleado":
        subsidio = 300000
    elif condicion_laboral == "empleado":
        subsidio = 250000
elif quintil == 3:
    if condicion_laboral == "desempleado":
        subsidio = 200000
    elif condicion_laboral == "empleado":
        subsidio = 150000

# Aplicar bonos adicionales
if quintil in [1, 2]:
    bono_adicional += 50000
if edad >= 60:
    bono_adicional += 30000

# Calcular subsidio total
total_subsidio = subsidio + bono_adicional

# Mostrar resultado
print(f'El valor del subsidio de arriendo es: {total_subsidio}')
