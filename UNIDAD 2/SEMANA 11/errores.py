"""
try:

    a = 4
    b = 0
    d = 4
    e = '4'    
    c = a / b
    print(f'El resultado de la division es: {c}')

    f = d + e
    print(f'La suma es: {f}')   

except ZeroDivisionError:
    print('No puede dividir por cero...')

except TypeError:
    print('No puede sumar numeros con string')

except:
    print('Aqui cualquier tipo de error')

finally: # el finally es opcional y siempre se ejecutará
          # exista un error o no...
          print('siempre se ejecuta')
"""

try:
    a = 4
    b = 0
    c = a / b
    print(f'El resultado de la división es: {c}')
except ZeroDivisionError:
    print('No puede dividir por cero...')

try:
    d = 4
    e = '4'
    f = d + e
    print(f'La suma es: {f}')
except TypeError:
    print('No puede sumar números con string')

finally:
    print('siempre se ejecuta')