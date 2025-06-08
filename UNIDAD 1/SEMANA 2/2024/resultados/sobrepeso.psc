Algoritmo sobrepeso
	
	Definir peso,estatura,IMC como Real;
	
	Escribir "Ingrese su peso (kg): ";
	Leer peso;
	
	Escribir "Ingrese su estatura (m): ";
	Leer estatura;
	
	IMC = peso / (estatura * estatura);
	
	Escribir "Su IMC es: ", IMC;
	
	Si IMC > 25 entonces
		Escribir "Usted tiene sobrepeso."
	Sino
		Escribir "Usted tiene un peso normal."
	FinSi
	
FinAlgoritmo
