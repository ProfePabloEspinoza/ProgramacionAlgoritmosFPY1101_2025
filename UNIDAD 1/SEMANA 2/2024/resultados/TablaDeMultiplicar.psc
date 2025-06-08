Algoritmo TablaDeMultiplicar
    Definir numero, resultado Como Entero
	
    Escribir "Ingrese un número positivo:"
    Leer numero
	
    Si numero > 0 Entonces
        Para multiplicador = 1 Hasta 10 Con Paso 1 Hacer
            resultado = numero * multiplicador
            Escribir numero, " x ", multiplicador, " = ", resultado
        FinPara
    Sino
        Escribir "El número ingresado no es válido. Por favor, ingrese un número positivo."
    FinSi
	
FinAlgoritmo

