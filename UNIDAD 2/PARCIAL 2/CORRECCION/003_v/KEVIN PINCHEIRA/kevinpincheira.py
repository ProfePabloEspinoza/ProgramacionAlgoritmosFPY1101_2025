
promedio = float(input('Ingrese su promedio: '))
decil = int(input('ingrese su decil del (1-4): '))

descuento=0.0
valor_matricula=95000
valor_arancel=2200000



if promedio >=6.5:
    decil = 1-2
    descuento= 0.25
elif promedio >=6.5:
    decil =3-4
    descuento=0.18
elif promedio <5.5<6.5:
    decil = 1-2
    descuento=0.15
elif promedio <5.5 <6.5:
    decil = 3-4
    descuento=0.12
elif decil >= 1-2-3:
    descuento=0.12
elif promedio >=6.0:
    decil= 1-2-3-4
    descuento=0.18+0.05
else:
    promedio<=5.4 or decil>=5
    print('No cumple con los requisitos: ')

#calcular descuento
valor_total=valor_matricula * (1-descuento)
valor_total_arancel=valor_arancel * (1-descuento)
print (f'El valor de su matricula más arancel con el descuento aplicado es: {valor_total_arancel}')
print (f'El valor de su matricula es: {valor_total}')
