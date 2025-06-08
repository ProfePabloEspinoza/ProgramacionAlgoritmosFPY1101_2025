
beneficio_arancel= float ()
beneficio_matricula= float ()
valor_carrera_final= int ()
valor_matricula_final = int ()


print("PROGRAMA DE BENEFICIOS ESTUDIANTILES")

print("Ingrese el valor del arancel de su carrera")
valor_carrera= int (input(""))

print("Ingrese el valor de la matricula de su carrera")
valor_matricula= int (input(""))

print ("¿Cual es su promedio final del colegio?")
promedio = float (input(""))

print ("¿En que decil del grado socioeconomico se encuentra? (1-10)")
decil = int(input(""))

if (promedio >= 6.5) and (decil == 1 or decil == 2):

    beneficio_arancel= beneficio_arancel + 0.25
    beneficio_matricula= beneficio_matricula + 0.12 + 0.05

    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)

    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula_final)
    

elif (promedio >= 6.5) and (decil == 3):

    beneficio_arancel= beneficio_arancel + 0.18
    beneficio_matricula= beneficio_matricula + 0.12 + 0.05

    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)

    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula_final)


elif (promedio >= 6.5) and (decil == 4):

    beneficio_arancel= beneficio_arancel + 0.18
    beneficio_matricula= beneficio_matricula + 0.05

    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)

    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula_final) 


if (promedio >= 5.5 or promedio<6) and (decil == 1 or decil == 2):
    
    beneficio_arancel= beneficio_arancel + 0.15
    beneficio_matricula= beneficio_matricula + 0.12 


    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)


    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula) 


if (promedio<=6.5) and (decil == 1 or decil == 2):

    beneficio_arancel= beneficio_arancel + 0.15
    beneficio_matricula= beneficio_matricula + 0.12 + 0.05

    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)

    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula_final) 


if (promedio >= 5.5 or promedio<6) and (decil == 3 ):

    beneficio_arancel= beneficio_arancel + 0.12
    beneficio_matricula= beneficio_matricula + 0.05

    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)

    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula) 


if (promedio<=6.5) and (decil == 3 ):

    beneficio_arancel= beneficio_arancel + 0.12
    beneficio_matricula= beneficio_matricula + 0.12 + 0.05

    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)

    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula) 


if (promedio >= 5.5 or promedio<6) and (decil == 4 ):

    beneficio_arancel= beneficio_arancel + 0.12
    

    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)

    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula_final)


if (promedio<=6.5) and (decil == 4 ):

    beneficio_arancel= beneficio_arancel + 0.12
    beneficio_matricula= beneficio_matricula + 0.05

    #calculo del valor de los aranceles y matricula

    valor_carrera_final= valor_carrera - (valor_carrera * beneficio_arancel)
    valor_matricula_final= valor_matricula - (valor_matricula * beneficio_matricula)

    print("El valor final del arancel es de", valor_carrera_final)
    print("El valor final de la matricula es de", valor_matricula) 
























