Algoritmo CalcularIMC
    // Definir variables
    Definir peso, estatura, imc Como Real
	
    // Solicitar al usuario que ingrese el peso en kilogramos
    Escribir "Ingrese su peso en kilogramos:"
    Leer peso
	
    // Solicitar al usuario que ingrese la estatura en metros
    Escribir "Ingrese su estatura en metros:"
    Leer estatura
	
    // Calcular el IMC
    imc = peso / (estatura * estatura)
	
    // Mostrar el IMC calculado
    Escribir "Su Índice de Masa Corporal (IMC) es:", imc
	
    // Determinar si la persona está en sobrepeso
    Si imc >= 25 Entonces
        Escribir "Usted está en sobrepeso."
    Sino
        Escribir "Usted no está en sobrepeso."
    FinSi
FinAlgoritmo

