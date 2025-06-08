Algoritmo Num_mayor
	
Definir num1, num2, num3 como Entero;
	
Escribir "Ingrese el primer número: ";
Leer num1;
	
Escribir "Ingrese el segundo número: ";
Leer num2;
	
Escribir "Ingrese el tercer número: ";
Leer num3;
	
Si num1 > num2 y num1 > num3 entonces
	Escribir "El mayor número es: ", num1;
fin si

Si num2 > num1 y num2 > num3 entonces
	Escribir "El mayor número es: ", num2;
fin si
		
Si num3 > num1 y num3 > num2 entonces
		Escribir "El mayor número es: ", num3;
FinSi
	
FinAlgoritmo
