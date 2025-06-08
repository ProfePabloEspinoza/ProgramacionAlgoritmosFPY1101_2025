Algoritmo CalculoDeSolemnes_Ponderado
	Definir nota, porcentaje, promedio, suma_ponderada Como Real
	Definir cantidad_notas, i Como Entero
	
	suma_ponderada=0
	promedio=0
	
	Escribir "Define la cantidad de notas: "
	leer cantidad_notas
	
	para i=1 hasta cantidad_notas Hacer
		Escribir "Ingrese Nota de la solemne ", i, ":"
		leer nota
		
		Escribir "Ingrese porcentaje de la nota ", i, " (Ej: 30 para 30%):"
		leer porcentaje
		
		suma_ponderada = suma_ponderada + (nota * porcentaje / 100)
		
	FinPara
	
	promedio = suma_ponderada
	
	si promedio >= 4.0 Entonces
		Escribir "Alumno Aprobo con nota: ", promedio
	SiNo
		Escribir "Alumno Reprobo con nota: ", promedio
	FinSi
	
FinAlgoritmo

