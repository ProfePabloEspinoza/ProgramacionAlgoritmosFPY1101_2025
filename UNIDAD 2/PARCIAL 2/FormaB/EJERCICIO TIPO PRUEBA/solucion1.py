# Solicitar datos de entrada
salario_base = float(input('Ingrese salario base: '))
desempeno = float(input('Ingrese puntuación de desempeño (1.0-7.0): '))
antiguedad = int(input('Ingrese años de antigüedad: '))

# Inicializar variables de bonificación
bonificacion_porcentual = 0.0
bono_extra = 0.0

# Calcular bonificación porcentual según las reglas
if desempeno > 6.0:
    if antiguedad >= 5:
        bonificacion_porcentual = 0.20
    else:
        bonificacion_porcentual = 0.15
elif 5.0 <= desempeno <= 6.0:
    if antiguedad >= 5:
        bonificacion_porcentual = 0.12
    else:
        bonificacion_porcentual = 0.08
else: # Desempeño < 5.0
    bonificacion_porcentual = 0.05

# Verificar condición para bono extra
if desempeno >= 6.5 and antiguedad >= 10:
    bono_extra = 50000.0

# Calcular bonificación total
bonificacion_total = (salario_base * bonificacion_porcentual) + bono_extra

# Mostrar resultado
print('El monto de la bonificación es:', bonificacion_total)