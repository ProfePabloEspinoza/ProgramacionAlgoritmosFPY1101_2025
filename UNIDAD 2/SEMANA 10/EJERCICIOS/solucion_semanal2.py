# Precios de las entradas por categoría
precio_nino = 3500
precio_adulto = 6000
precio_adulto_mayor = 4000

# Contadores para cada categoría de entrada y subtotales
cantidad_ninos = 0
cantidad_adultos = 0
cantidad_adultos_mayores = 0

subtotal_ninos = 0
subtotal_adultos = 0
subtotal_adultos_mayores = 0

total_a_pagar = 0

print("¡Bienvenido al sistema de cálculo de entradas de cine!")

# Solicitar cantidad de personas con validación básica
num_personas_str = input("Ingrese la cantidad de personas en el grupo: ")

# Validar que sea un dígito y mayor que cero
while not num_personas_str.isdigit() or int(num_personas_str) <= 0:
    print("Entrada no válida. Por favor, ingrese un número entero positivo.")
    num_personas_str = input("Ingrese la cantidad de personas en el grupo: ")

num_personas = int(num_personas_str)


for i in range(num_personas):
    print(f"\n--- Persona {i + 1} ---")
    
    # Solicitar edad con validación básica
    edad_str = input(f"Ingrese la edad de la persona {i + 1}: ")

    # Validar que sea un dígito y no negativo
    while not edad_str.isdigit() or int(edad_str) < 0:
        print("Entrada no válida. Por favor, ingrese un número entero no negativo para la edad.")
        edad_str = input(f"Ingrese la edad de la persona {i + 1}: ")

    edad = int(edad_str)

    if edad < 13:
        print(f"Categoría: Niño, Precio: ${precio_nino}")
        cantidad_ninos += 1
        subtotal_ninos += precio_nino

    elif edad >= 13 and edad <= 64: # También se puede escribir como: 13 <= edad <= 64
        print(f"Categoría: Adulto, Precio: ${precio_adulto}")
        cantidad_adultos += 1
        subtotal_adultos += precio_adulto

    else: # edad >= 65
        print(f"Categoría: Adulto Mayor, Precio: ${precio_adulto_mayor}")
        cantidad_adultos_mayores += 1
        subtotal_adultos_mayores += precio_adulto_mayor

total_a_pagar = subtotal_ninos + subtotal_adultos + subtotal_adultos_mayores

print("\n--- DETALLE DE LA COMPRA ---")
print("-----------------------------")

if cantidad_ninos > 0:
    print(f"Entradas Niño (Menores de 13 años): {cantidad_ninos} x ${precio_nino} = ${subtotal_ninos}")

if cantidad_adultos > 0:
    print(f"Entradas Adulto (13-64 años):       {cantidad_adultos} x ${precio_adulto} = ${subtotal_adultos}")

if cantidad_adultos_mayores > 0:
    print(f"Entradas Adulto Mayor (65+ años):   {cantidad_adultos_mayores} x ${precio_adulto_mayor} = ${subtotal_adultos_mayores}")

print("-----------------------------")
print(f"TOTAL A PAGAR: ${total_a_pagar}")
print("-----------------------------")
print("¡Gracias por su compra!")