print("segundo ejercicio: n/2")

import random
num1=int(input("Ingrese numero inferior:"))
num2=int(input("Ingrese numero superior"))
print("") 
if num1<num2:
    correcto=False
    medio=int((num1+num2) /2)
    ajuste=int((num2-num1) *0.2)
    numero=random.randrange(ajuste,medio)

    test1=int(input("intente adivinar:"))
    if test1==numero:
        print("Felicitaciones , adivino el primer intento.")
        correcto=True 

    else:#SEGUNDO INTENTO
        if numero>test1:
            print("El número es mayor. ")
        else :
            print("el numero es menor. ")  

        print("")  
        test2=int(input("Intente denuevo:"))    
        if test2==numero and correcto==False: 
            print ("Felicitaciones, adivino en el segundo Intento .")
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
    print("el valor 1 debe ser menor al segundo, corre el programa una vez mas .")   
