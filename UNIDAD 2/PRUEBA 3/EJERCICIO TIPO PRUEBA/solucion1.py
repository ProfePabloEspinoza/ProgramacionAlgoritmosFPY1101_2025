"""
¿En qué se parece al algoritmo para detectar números primos?
Muy buena pregunta para clase. Aquí te explico claramente para ti y cómo podrías decírselo a 
tus alumnos:

Verificación	Explicación	Ejemplo
Número primo	Tiene solo 2 divisores: 1 y él mismo	7 → divisores: 1, 7
Código válido (de este ejercicio)	Tiene exactamente 3 divisores	49 → divisores: 1, 7, 49

📌 Entonces:
En ambos casos, el programa cuenta cuántos divisores tiene un número.

El algoritmo es exactamente el mismo hasta que se hace la comparación:

Si divisores == 2 → primo.

Si divisores == 3 → válido para la bóveda.

✅ Esta es una gran oportunidad para enseñar la lógica de divisibilidad, mostrando que se 
puede reutilizar el mismo algoritmo para distintos fines.
"""
# Pedimos cuántos códigos se van a verificar
while True:
    try:
        cantidad = int(input("¿Cuántos códigos desea verificar?: "))
        break
    except:
        print("Debe ingresar un número entero.")

# Contadores
validos = 0
invalidos = 0

# Ingreso de cada código
for i in range(1, cantidad + 1):
    while True:
        try:
            codigo = int(input(f"Ingrese código {i}: "))
            if codigo > 10:
                break
            else:
                print("Debe ser un número mayor que 10.")
        except:
            print("Debe ingresar un número entero.")

    # Contamos cuántos divisores tiene el número
    cantidad_divisores = 0
    for j in range(1, codigo + 1): 
        if codigo % j == 0:  # Cuando codigo % j == 0, significa que j es un divisor de codigo.
            cantidad_divisores += 1
            
            """
            Si codigo es 49:
            

                Cuando j es 1: 49 % 1 == 0 (1 es divisor de 49)
                Cuando j es 7: 49 % 7 == 0 (7 es divisor de 49)
                Cuando j es 49: 49 % 49 == 0 (49 es divisor de 49, es decir, es divisible por sí mismo)             
            
            """

    # Si tiene exactamente 3 divisores, es válido
    if cantidad_divisores == 3:
        print("Código válido.")
        validos += 1
    else:
        print("Código inválido.")
        invalidos += 1

# Mostramos los resultados
print(f"\nSe ingresaron {validos} códigos válidos.")
print(f"Se ingresaron {invalidos} códigos inválidos.")
