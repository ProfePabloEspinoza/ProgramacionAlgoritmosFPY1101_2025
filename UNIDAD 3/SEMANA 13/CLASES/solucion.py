"""
#Solución Ejercicio 1

viaje = [
    ["Carlos", ["carpa", "saco de dormir", "linterna"]],
    ["Ana", ["mochila", "comida", "botiquín"]],
    ["Luis", ["parrilla", "carbón", "bebidas"]],
    ["Sofía", ["mapa", "snacks", "ropa extra"]]
]

presupuesto = [25000, 30000, 27000, 22000]

print("Segundo ítem del tercer amigo:", viaje[2][1][1])
print("Presupuesto del primer amigo:", presupuesto[0])
print("Último ítem del segundo amigo:", viaje[1][1][-1])
print("Ítems del último amigo:", viaje[-1][1])

"""

#Solución Ejercicio 2

viaje = []
presupuesto = []

n = int(input("¿Cuántos amigos irán al viaje? "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del amigo {i+1}: ")
    items = []
    for j in range(3):
        item = input(f"Ingrese el ítem {j+1} que llevará {nombre}: ")
        items.append(item)
    viaje.append([nombre, items])

    monto = int(input(f"Ingrese el presupuesto de {nombre}: "))
    presupuesto.append(monto)

while True:
    print("\n--- MENÚ ---")
    print("1. Ver lo que lleva un amigo")
    print("2. Ver presupuesto de un amigo")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        nombre_buscar = input("Ingrese el nombre del amigo: ")
        encontrado = False
        
        """                   
            Imaginemos que tienes esta lista:
            
            viaje = [
                ["Carlos", ["carpa", "saco", "linterna"]],
                ["Ana", ["mochila", "comida", "botiquín"]],
                ["Luis", ["parrilla", "carbón", "bebidas"]]
            ]
            Cada elemento de la lista viaje representa una persona, por ejemplo:
           
            persona = ["Ana", ["mochila", "comida", "botiquín"]]
            Entonces, si tú escribes:

            persona[0]
            Estás accediendo a "Ana" (porque es el primer elemento de la sublista persona).

            🔎 Entonces, ¿qué hace esta línea?
            
            if persona[0] == nombre_buscar:
            
            Si el nombre de la persona actual (persona[0]) es igual al nombre que me dijo 
            el usuario (nombre_buscar), entonces ¡encontré a la persona!

            🧠 Ejemplo real
           
            nombre_buscar = "Ana"

            for persona in viaje:
                if persona[0] == nombre_buscar:
                    print(f"{persona[0]} lleva:", persona[1])
            📌 En este caso:

            persona[0] es "Ana"
            nombre_buscar es "Ana"
            Entonces entra al if y muestra lo que lleva "Ana".

            🎓 Versión para explicar en clase
            Podrías decir:

            “Estamos recorriendo una lista de amigos (viaje). 
            Cada amigo tiene un nombre y una lista de cosas que lleva. 
            En cada vuelta del ciclo, revisamos si el nombre del amigo
            (persona[0]) es igual al nombre que el usuario escribió (nombre_buscar).
            Si coincide, mostramos lo que lleva.”
        
        """
        for persona in viaje: # formamos una sublista persona persona = ["Ana", ["mochila", "comida", "botiquín"]]
            if persona[0].lower() == nombre_buscar.lower():
                print(f"{nombre_buscar} lleva: {persona[1]}")
                encontrado = True
                break
        if not encontrado:
            print("Ese nombre no está en la lista.")

    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre del amigo: ")
        encontrado = False
        for i in range(len(viaje)):
            if viaje[i][0].lower() == nombre_buscar.lower():
                print(f"{nombre_buscar} tiene un presupuesto de: ${presupuesto[i]}")
                encontrado = True
                break
        if not encontrado:
            print("Ese nombre no está en la lista.")

    elif opcion == "3":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")

