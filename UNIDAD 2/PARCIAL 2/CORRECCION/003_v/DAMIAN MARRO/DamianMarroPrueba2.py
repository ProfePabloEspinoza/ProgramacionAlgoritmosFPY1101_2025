conAcademica = float (input("ingrese su promedio academico:  "))

conSEconomica = float (input("en que decil pertenece su grupo familiar?  "))

valorArancel = int(2200000)
matricula = 95000


if conAcademica >= 6.5 and conSEconomica <= 2:
    VFinal = valorArancel * 0.25 
    print (f"su valor arancer es: {valorArancel - VFinal }")
    if conAcademica <= 3:
        descMatricula = matricula * 0.12
        print (f"su valor matricula es de {descMatricula - matricula}")   
        if conAcademica >= 6.0:
            adicional = matricula * 0.05
            adicional = valorArancel * 0.05
            print (f"tiene un 5 por ciento de descuento en su arance {valorArancel - adicional}")
            print (f"tiene un 5 por ciento de descuento en su matricula de {adicional - matricula}")         

    
elif conAcademica >= 6.5 and 3 <= conSEconomica >= 4 :
    VFinal = valorArancel * 0.18 
    print (f"su valor arancer es: {valorArancel - VFinal}")
    if conAcademica <= 3:
        descMatricula = matricula * 0.12
        print (f"su valor matricula es de {descMatricula - matricula}")   
        if conAcademica >= 6.0:
            adicional = matricula * 0.05
            adicional = valorArancel * 0.05
            print (f"tiene un 5 por ciento de descuento en su arance {valorArancel - adicional}")
            print (f"tiene un 5 por ciento de descuento en su matricula de {adicional - matricula}")         

elif 5.5 >= conAcademica <= 6.5 and 1 >= conSEconomica <= 2:
    VFinal = valorArancel * 0.15 
    print (f"su valor arancer es: {valorArancel - VFinal}")
    if conAcademica <= 3:
        descMatricula = matricula * 0.12
        print (f"su valor matricula es de {descMatricula - matricula}")   
        if conAcademica >= 6.0:
            adicional = matricula * 0.05
            adicional = valorArancel * 0.05
            print (f"tiene un 5 por ciento de descuento en su arance {valorArancel - adicional}")
            print (f"tiene un 5 por ciento de descuento en su matricula de {adicional - matricula}")         

elif 5.5 >= conAcademica <= 6.5 and 3 >= conSEconomica <= 4:
    VFinal = valorArancel * 0.12 
    print (f"su valor arancer es: {valorArancel - VFinal}")
    if conAcademica <= 3:
        descMatricula = matricula * 0.12
        print (f"su valor matricula es de {descMatricula - matricula}")
        if conAcademica >= 6.0:
            adicional = matricula * 0.05
            adicional = valorArancel * 0.05
            print (f"tiene un 5 por ciento de descuento en su arance {valorArancel - adicional}")
            print (f"tiene un 5 por ciento de descuento en su matricula de {adicional - matricula}")         
else:
    print ("ingrese un valor dentro del rango")    