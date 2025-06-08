Algoritmo CalculoDeSolemnes
	
	Definir nota, promedio, suma_nota, porcentaje Como Real
	Definir cantidad_notas, i Como Entero
	
	nota = 0
	promedio = 0
	suma_nota = 0
	
	Escribir "Define la cantidad de notas: ";
	leer cantidad_notas
	
	
	para i = 1 hasta cantidad_notas Hacer
		
		escribir "Ingrese Nota de la solemne ",i, ":";
		leer nota;
		
		Escribir "Ingrese el porcentaje de la nota de la solemne ",i, "(Ej: 30 para 30%)";
		leer porcentaje;
		
		suma_nota = suma_nota + (nota * porcentaje / 100);
		
		
	FinPara
	
	promedio = suma_nota;
	
	si promedio >= 4.0 Entonces		
		escribir "Alumno Aprobo con nota: ", promedio
	SiNo
		Escribir "Alumno Reprobo con nota: ", promedio
		
	FinSi
	
FinAlgoritmo
