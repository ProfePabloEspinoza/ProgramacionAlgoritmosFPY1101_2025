# --- Ejemplo de if/elif/else con Razas de Perros ---

mascota = input("¿Qué mascota tienes? (perro/gato/pez): ").lower() # Convertimos a minúsculas para comparar fácil

if mascota == "perro":
    print("¡Guau! Los perros son geniales.")
    # Preguntamos la raza específica del perro
    raza = input("¿Qué raza es tu perro? (Ej: Labrador, Bulldog, Poodle, Pastor Alemán): ").lower()

    # Usamos if/elif/else anidado para dar información de la raza
    if raza == "labrador":
        print("Temperamento del Labrador: Amigable, extrovertido y dócil. ¡Muy inteligentes y buenos para familias!")
    elif raza == "bulldog":
        print("Temperamento del Bulldog: Calmado, valiente y amigable, aunque a veces un poco testarudo. ¡Mucha personalidad!")
    elif raza == "poodle" or raza == "caniche": # Podemos aceptar varios nombres
        print("Temperamento del Poodle/Caniche: Muy inteligente, activo y elegante. Aprenden rápido.")
    elif raza == "pastor alemán":
        print("Temperamento del Pastor Alemán: Leal, seguro de sí mismo, valiente y muy inteligente. ¡Excelentes guardianes!")
    elif raza == "chihuahua":
        print("Temperamento del Chihuahua: Vivaz, alerta y con una gran personalidad en un cuerpo pequeño.")
    # Puedes añadir más razas aquí con 'elif'
    # ...
    else:
        # Si la raza no está en nuestra lista, damos un mensaje general
        print(f"No tengo información específica sobre la raza '{raza}', ¡pero seguro que es un perro fantástico!")

elif mascota == "gato":
    print("¡Miau! Un felino muy elegante y misterioso.")
    # Podrías anidar otro if/elif aquí si quisieras preguntar sobre razas de gatos

elif mascota == "pez":
    print("¡Glup! Silencioso pero relajante.")

else:
    # Si no es perro, gato ni pez
    print(f"Vaya, no conozco mucho sobre las mascotas '{mascota}'.")

print("\n--- Fin del programa ---")