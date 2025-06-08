Proceso Promedio_de_Alumno
	
	Definir Nota, suma_nota, Promedio Como Real;
	Definir Nombre Como Caracter;
	Definir i Como Entero;
	
	Nota = 0;
	suma_nota = 0;
	
	
	para i = 1 Hasta 3 Hacer
		escribir "ingrese  la nota:", i;
		Leer nota;
		suma_nota = suma_nota + Nota;
		
	FinPara
	Promedio = suma_nota / 3;
	
	si Promedio >= 4.0 Entonces
		Escribir "aprobo con un: ", Promedio;
		
	SiNo
		Escribir "reprobo con un: ", Promedio;
	FinSi
	
	
	
	
FinProceso
