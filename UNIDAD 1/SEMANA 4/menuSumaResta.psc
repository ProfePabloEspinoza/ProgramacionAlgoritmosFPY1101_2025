Proceso menuSumaResta
    // Regla de negocio 1: Declaraci�n de variables
    Definir contador, limite, suma, resta, numero1, numero2, opciones Como Entero;
	
    // Regla de negocio 2: Inicializaci�n
    opciones = 0;
    suma = 0
    resta = 0
	
    // Men� de opciones
    Escribir "Men� de Opciones:"
    Escribir "1. Restar valores"
    Escribir "2. Sumar valores"
    Escribir "3. Salir"
    
    // Regla de negocio 2.1: Leer opci�n
    Escribir "Seleccione una opci�n (1, 2 o 3):"
    Leer opciones
	
    // Regla de negocio 2.2: Evaluar opci�n
    Si opciones = 1 Entonces
        // Regla de negocio 2.2.1: Resta
        Escribir "Ingrese el primer n�mero:"
        Leer numero1
        Escribir "Ingrese el segundo n�mero:"
        Leer numero2
        resta <- numero1 - numero2
        Escribir "La resta es: ", resta
		
    Sino
        Si opciones = 2 Entonces
            // Regla de negocio 2.2.2: Suma
            Escribir "Ingrese el primer n�mero:"
            Leer numero1
            Escribir "Ingrese el segundo n�mero:"
            Leer numero2
            suma <- numero1 + numero2
            Escribir "La suma es: ", suma
			
        Sino
            Si opciones = 3 Entonces
                // Regla de negocio 2.2.3: Salir
                Escribir "Saliendo del programa."
            Sino
                // Si escribe otra opci�n
                Escribir "Opci�n no v�lida."
            FinSi
        FinSi
    FinSi
	
    // Regla de negocio 4: Fin del proceso
FinProceso

