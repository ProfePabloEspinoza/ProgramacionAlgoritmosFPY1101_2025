salario = int(input('Ingrese su sueldo base: '))

desempeno = float(input('Ingrese el desempñeo entre (1.0 - 7.0): '))

antiguedad = int(input('Ingrese la entiguedad: '))



bonificacion = 0.0

bono_extra = 0.0

bonificacion_tota = 0.0



if desempeno > 6.0:

  if antiguedad >= 5:

    bonificacion = 0.20

  else:

    bonificacion = 0.15

elif 5.0 <= desempeno <= 6.0:

  if antiguedad >= 5:

    bonificacion = 0.12

  else:

    bonificacion = 0.08

else: # = desepeño < 5.0

  bonificacion = 0.05



# bono extra



if desempeno > 6.5 and antiguedad >= 10:

  bono_extra = 50000



bonificacion_tota = (salario * bonificacion) + bono_extra



print(f'El monto de la bonificacion total es: {bonificacion_tota}')

