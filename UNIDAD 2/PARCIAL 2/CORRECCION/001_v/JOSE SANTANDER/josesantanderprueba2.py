print("primer ejercicio: \n")
prom=float(input("ingrese su promedio: "))
decil=int(input("ingrese el decil (1-10): "))
descuentomatricula=1.0
descuento=1.00

arancel=2_200_000
matricula=95_000


if prom>6.5 and (1<=decil<=2):
    descuento = 0.75
elif prom>6.5 and (3<=decil<=4):
    descuento=0.82
elif (5.5 < prom <= 6.5) and (1<=decil<=2):
    descuento=0.85
elif (5.5 < prom <= 6.5) and (3<=decil<=4):
    descuento=0.88

if decil==1 or decil==2 or decil==3:
    descuentomatricula-=0.12
    if prom >= 6.0:
        descuentonota=0.05
        print(descuentomatricula)

print("El valor del arancel es:", int(arancel*descuento))
print("El valor de la matrícula es:",int(matricula*descuentomatricula))


print("-"*20)
print("segundo ejercicio: \n")

import random
num1=int(input("ingrese limite inferior: "))
num2=int(input("ingrese limite superior: "))
print("")
if num1<num2:
    correcto=False
    medio=int((num1+num2) / 2)
    ajuste=int((num2-num1)*0.2)
    numero=random.randrange(ajuste,medio)

    test1=int(input("intente adivinar: "))
    if test1==numero:
        print("Felicitaciones, adivinó en el primer intento.")
        correcto=True

    else:#segundo intento

        if numero>test1:
            print("el numero es mayor.")
        else:
            print("el numero es menor.")

        print("")
        test2=int(input("intente de nuevo: "))
        if test2==numero and correcto==False:
            print("Felicitaciones, adivinó en el segundo intento.")
            correcto=True
            
        else:#tecer intento
            if numero>test2:
                print("el numero es mayor.")
                if (numero-test1)<(numero-test2):
                    print("Te daré una pista:")
                    print("El número que buscas está más cerca de",test1,"que de ",test2)
                else:
                    print("Te daré una pista:")
                    print("El número que buscas está más cerca de",test2,"que de ",test1)

            else:
                print("el numero es menor.")
                if (numero-test1)<(numero-test2):
                    print("Te daré una pista:")
                    print("El número que buscas está más cerca de",test1,"que de ",test2)
                else:
                    print("Te daré una pista:")
                    print("El número que buscas está más cerca de",test2,"que de ",test1)

            print("")
            test3=int(input("intente la ultima vez: "))
            if test3==numero and correcto==False:
                print("Felicitaciones, adivinó en su tercer intento.")
            else:
                print("Perdiste.")
                print("El número era:",numero)
else:
    print("el valor 1 debe ser menor al segundo, corre el programa una vez mas.")