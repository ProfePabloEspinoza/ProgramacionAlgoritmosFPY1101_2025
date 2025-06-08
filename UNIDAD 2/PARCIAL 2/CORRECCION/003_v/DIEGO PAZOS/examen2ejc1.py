arancelbase=int(input("Ingrese el arancel base: "))
matricula=int(input("Ingrese el monto de la matricula: "))
promedio=float(input("Ingrese el promedio: "))
decil=int(input("Ingrese el decil socioeconomico: "))

if promedio>6.5 and (decil==1 or decil==2):
    arancel=arancelbase*0.25
    arancelfianl=arancelbase-arancel
    print("El arancel es: ", arancelfianl)
elif promedio>6.5 and (decil==3 or decil==4):
    arancel=arancelbase*0.18
    arancelfianl=arancelbase-arancel
    print("El arancel es: ", arancelfianl)
elif 5.5<promedio<=6.5 and (decil==1 or decil==2):
    arancel=arancelbase*0.15
    arancelfianl=arancelbase-arancel
    print("El arancel es: ", arancelfianl)
elif 5.5<promedio<=6.5 and (decil==3 or decil==4):
    arancel=arancelbase*0.12
    arancelfianl=arancelbase-arancel
    print("El arancel es: ", arancelfianl)
else:
    arancel=arancelbase*0
    arancelfianl=arancelbase-arancel
    print("El arancel es: ", arancelbase)

if (decil ==1 or decil ==2 or decil ==3) and promedio >=6:
    descuento = matricula *0.12
    matriculafinal = matricula - descuento
    descuentoadicional = matriculafinal *0.05
    matriculafinal = matriculafinal - descuentoadicional
    print("El monto de la matricula es:", matriculafinal)
elif decil ==1 or decil ==2 or decil ==3:
    descuento = matricula *0.12
    matriculafinal = matricula - descuento
    print("El monto de la matricula es:", matriculafinal)

