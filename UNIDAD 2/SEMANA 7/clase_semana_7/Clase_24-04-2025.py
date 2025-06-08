"""
num1 = int(input('Ingrese el primer número: ')) 
num2 = int(input('Ingrese el segundo número: ') )


suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2 


# print('El valor de num1 es: ',num1)
# print(f'El valor de num1 es: {num1}')

print(f'La suma entre {num1} + {num2} = {suma}')
#print('la suma entre ', num1, ' + ',num2, ' = ', suma)
print(f'La resta entre {num1} - {num2} = {resta}')
print(f'La Multiplicación entre {num1} x {num2} = {multi}')
print(f'La division entre {num1} / {num2} = {div}')

"""

nombre = input('Ingrese su nombre: ')
edad = int(input(f'{nombre} Ingresa tu edad: '))

if edad >= 18:
    print(f'{nombre} eres MAYOR de Edad')
else:
    print(f'{nombre} eres MENOR de Edad')