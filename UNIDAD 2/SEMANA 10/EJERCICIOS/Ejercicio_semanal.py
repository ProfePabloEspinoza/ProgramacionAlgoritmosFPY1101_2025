desea = input('Desea comprar (S/N)')
subtotal = 0
total = 0


while desea == 'S' or desea == 's':

    cant = int(input('Cantidad de bultos: '))

    peso = int(input('peso bulto(kg): '))

    if 0 < peso <= 5:
        valor = 1000
        opcion = 'LIVIANO'
        subtotal = valor * cant
        mensaje_liviano = f'{cant} bulto {opcion}   ${subtotal}'

    elif 6 <= peso <= 10:
        valor = 4500
        opcion = 'NORMAL'
        subtotal = valor * cant
        mensaje_normal = f'{cant} bulto {opcion}   ${subtotal}'

    elif peso >= 11:
        valor = 8000
        opcion = 'PESADO'
        subtotal = valor * cant
        mensaje_pesado = f'{cant} bulto {opcion}   ${subtotal}'

    else:
        print('Peso Inválido')

    total = total + subtotal

    desea = input('Desea comprar (S/N)')

print('       ENCOMIENDAS                    ')
print('______________________________________')
print(f'{mensaje_liviano}')
print(f'{mensaje_normal}')
print(f'{mensaje_pesado}')
print('_______________________________________')
print('')
print(f'                     Total: ${total}')







