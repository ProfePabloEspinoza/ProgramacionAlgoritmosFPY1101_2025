print("ejercicio 1 : ")
prom=float(input("ingrese su promedio: "))
decil=int(input("Ingrese el decil (1-10)"))
descuentomatricula= 1.0 
descuento=1.00


arancel=2_200_000
matricula=95_000

if prom>6.5 and (1<=decil<=2):
    descuento = 0.25 
elif prom>6.5 and (3<=decil<=4):
    descuento = 0.18
elif (5.5 < prom <= 6.5) and (1<= decil<= 2):
    descuento = 0.15 
elif (5.5 < prom <= 6.5) and (3<= decil <= 4):
    descuento = 0.12 

if decil==1 or decil==2 or decil==3:
    descuentomatricula = 0.12 
    if prom > 6.0:
        decuentonota= 0.5 
        print(descuentomatricula)

print("El valor arancel es:" , int (arancel*descuento)  ) 
print("el valor de la matricula es:",int(matricula*descuentomatricula))

print("-"*20)

