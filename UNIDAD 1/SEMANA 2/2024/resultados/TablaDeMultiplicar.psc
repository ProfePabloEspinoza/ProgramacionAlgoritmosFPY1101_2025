Algoritmo TablaDeMultiplicar
    Definir numero, resultado Como Entero
	
    Escribir "Ingrese un n�mero positivo:"
    Leer numero
	
    Si numero > 0 Entonces
        Para multiplicador = 1 Hasta 10 Con Paso 1 Hacer
            resultado = numero * multiplicador
            Escribir numero, " x ", multiplicador, " = ", resultado
        FinPara
    Sino
        Escribir "El n�mero ingresado no es v�lido. Por favor, ingrese un n�mero positivo."
    FinSi
	
FinAlgoritmo

