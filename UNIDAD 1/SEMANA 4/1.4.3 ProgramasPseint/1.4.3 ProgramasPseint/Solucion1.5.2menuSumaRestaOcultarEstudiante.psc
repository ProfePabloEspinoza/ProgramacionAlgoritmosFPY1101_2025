Proceso menuSumaResta
    Definir suma, resta, numero1,numero2, op como entero;
   
	op <- 0;
    suma <- 0;
	resta <- 0;
    
	Escribir "Men� de Opciones:";
	Escribir "1. Restar Valores";
	Escribir "2. Sumar valores";
	Escribir "3. Salir";
	Escribir "Seleccione una opci�n (1-3):";
	Leer op;
	
	Si op = 1 Entonces
		
		Escribir "Ingrese el primer n�mero para restar:";
		Leer numero1;
		Escribir "Ingrese el segundo n�mero para restar:";
		Leer numero2;
		resta <- numero1 - numero2;
		Escribir "La resta es: ", resta;
	Fin Si
	
	Si op = 2 Entonces
		
		Escribir "Ingrese el primer n�mero para sumar:";
		Leer numero1;
		Escribir "Ingrese el segundo n�mero para sumar:";
		Leer numero2;
		suma <- numero1 + numero2;
		Escribir "La suma es: ", suma;
	Fin Si
	
	Si op = 3 Entonces
		Escribir "Saliendo del programa.";
	Fin Si
	
	Si op <> 3 o op <> 1 o op <> 2 Entonces
		Escribir "Opci�n inv�lida.";
		
	Fin Si

FinProceso
