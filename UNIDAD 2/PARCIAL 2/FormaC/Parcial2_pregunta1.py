promedio = float(input('Ingrese su promedio: '))
decil = int(input('Ingrese el decil (1-10): '))
beca_academica = 0
bono_adicional = 0

# Definir becas según promedio y decil
if promedio > 6.5 and (decil == 1 or decil == 2):
    beca_academica = 200000
elif promedio > 6.5 and (decil == 3 or decil == 4):
    beca_academica = 150000
elif 5.5 < promedio <= 6.5 and (decil == 1 or decil == 2):
    beca_academica = 120000
elif 5.5 < promedio <= 6.5 and (decil == 3 or decil == 4):
    beca_academica = 100000

# Bono adicional según decil
if decil == 1 or decil == 2 or decil == 3:
    bono_adicional = 50000
    if promedio >= 6.0:
        bono_adicional += 30000  # Se suma el bono adicional si el promedio es mayor o igual a 6.0

# Calcular valor final de la beca
total_beca = beca_academica + bono_adicional

# Mostrar resultados
print(f'El valor de la beca de alimentación es: {total_beca}')

