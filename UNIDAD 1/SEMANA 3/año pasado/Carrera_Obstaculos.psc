Proceso Carrera_Obstaculos
    Definir respuesta como caracter
	
    Escribir "¡Comienza la carrera!"
	
    Escribir "¿Encuentras una valla? (si/no)"
    Leer respuesta
	
    Si respuesta = "si" Entonces
        Escribir "Debes saltar la valla."
    Sino
        Escribir "Continúa corriendo."
    FinSi
	
    Escribir "¿Encuentras un túnel? (si/no)"	
    Leer respuesta
	
    Si respuesta = "si" Entonces
        Escribir "Debes atravesar el túnel."
    Sino
        Escribir "Continúa corriendo."
    FinSi
	
    Escribir "¿Encuentras una laguna? (si/no)"
    Leer respuesta
	
    Si respuesta = "si" Entonces
        Escribir "Debes nadar."
        Escribir "Te agotas, te devuelves y pierdes la carrera."
    Sino
        Escribir "¡Felicidades! Has llegado a la meta con éxito."
    FinSi
	
FinProceso


