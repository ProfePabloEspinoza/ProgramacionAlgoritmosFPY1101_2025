Proceso menuSumaResta
    // Regla de negocio 1: Declaración de variables
    Definir contador, limite, suma, resta, numero1, numero2, opciones Como Entero;
	
    // Regla de negocio 2: Inicialización
    opciones = 0;
    suma = 0
    resta = 0
	
    // Menú de opciones
    Escribir "Menú de Opciones:"
    Escribir "1. Restar valores"
    Escribir "2. Sumar valores"
    Escribir "3. Salir"
    
    // Regla de negocio 2.1: Leer opción
    Escribir "Seleccione una opción (1, 2 o 3):"
    Leer opciones
	
    // Regla de negocio 2.2: Evaluar opción
    Si opciones = 1 Entonces
        // Regla de negocio 2.2.1: Resta
        Escribir "Ingrese el primer número:"
        Leer numero1
        Escribir "Ingrese el segundo número:"
        Leer numero2
        resta <- numero1 - numero2
        Escribir "La resta es: ", resta
		
    Sino
        Si opciones = 2 Entonces
            // Regla de negocio 2.2.2: Suma
            Escribir "Ingrese el primer número:"
            Leer numero1
            Escribir "Ingrese el segundo número:"
            Leer numero2
            suma <- numero1 + numero2
            Escribir "La suma es: ", suma
			
        Sino
            Si opciones = 3 Entonces
                // Regla de negocio 2.2.3: Salir
                Escribir "Saliendo del programa."
            Sino
                // Si escribe otra opción
                Escribir "Opción no válida."
            FinSi
        FinSi
    FinSi
	
    // Regla de negocio 4: Fin del proceso
FinProceso

