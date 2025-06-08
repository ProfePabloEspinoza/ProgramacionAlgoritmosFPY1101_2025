Algoritmo CalcularPromedio
    // Definir variables
    Definir cantidad_calificaciones, calificacion, promedio Como Real
    Definir suma_calificaciones Como Entero
	
    // Inicializar la suma de calificaciones
    suma_calificaciones = 0
	
    // Solicitar al usuario que ingrese la cantidad de calificaciones
    Escribir "Ingrese la cantidad de calificaciones:"
    Leer cantidad_calificaciones
	
    // Solicitar al usuario que ingrese cada calificación
    Para i = 1 Hasta cantidad_calificaciones Con Paso 1 Hacer
        Escribir "Ingrese la calificación ", i, ":"
        Leer calificacion
        suma_calificaciones = suma_calificaciones + calificacion
    FinPara
	
    // Calcular el promedio
    promedio = suma_calificaciones / cantidad_calificaciones
	
    // Mostrar el promedio calculado
    Imprimir  "El promedio de calificaciones es:", promedio
	
    // Determinar si el estudiante está aprobado o reprobado
    Si promedio >= 40 Entonces
        Imprimir  "¡Felicidades! Estás aprobado."
    Sino
        Imprimir  "Lo siento, estás reprobado."
    FinSi
FinAlgoritmo

