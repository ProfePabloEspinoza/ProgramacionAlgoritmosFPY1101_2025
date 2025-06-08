"""
PROGRAMA: Simulador Pomodoro Simple
¿QUÉ ES POMODORO?: Una técnica para estudiar mejor
- Estudias 25 minutos
- Descansas 5 minutos
- Repites el ciclo

CONCEPTOS QUE APRENDEREMOS:
- Variables para guardar información
- Condicionales (if/elif/else)
- Bucle while
- Contadores
"""

# ==================================
# PASO 1: Crear las variables
# ==================================
# Tiempos en minutos
tiempo_estudio = 25      # Cuántos minutos para estudiar
tiempo_descanso = 5      # Cuántos minutos para descansar

# Contadores
bloques_completados = 0  # Cuántos bloques de estudio hemos terminado

# Estado: ¿qué estamos haciendo?
# Puede ser: "esperando", "estudiando" o "descansando"
estado = "esperando"

# Mensaje de bienvenida
print("🍅 POMODORO - Técnica de Estudio 🍅")
print("Estudia mejor con bloques de tiempo")
print("Por defecto: 25 min estudio + 5 min descanso")

# ==================================
# PASO 2: Bucle principal
# ==================================
while True:
    # Mostrar información actual
    print("\n" + "="*40)
    print(f"Estado: {estado}")
    print(f"Bloques completados hoy: {bloques_completados}")
    print("="*40)
    
    # Menú simple
    print("\n¿QUÉ QUIERES HACER?")
    print("1. Cambiar tiempos (estudio/descanso)")
    print("2. Empezar a estudiar")
    print("3. Terminar actividad actual")
    print("4. Ver resumen")
    print("5. Salir")
    
    opcion = input("\nElige (1-5): ")
    
    # ==================================
    # OPCIÓN 1: Cambiar tiempos
    # ==================================
    if opcion == "1":
        print("\n--- CONFIGURAR TIEMPOS ---")
        print(f"Tiempo actual: {tiempo_estudio} min estudio, {tiempo_descanso} min descanso")
        
        # Pedir nuevo tiempo de estudio
        try:
            nuevo_estudio = input("¿Cuántos minutos quieres estudiar? ")
            nuevo_estudio = int(nuevo_estudio)
            
            if nuevo_estudio > 0:
                tiempo_estudio = nuevo_estudio
                print(f"✅ Tiempo de estudio: {tiempo_estudio} minutos")
            else:
                print("❌ El tiempo debe ser mayor que 0")
                
        except ValueError:
            print("❌ Debes escribir un número")
        
        # Pedir nuevo tiempo de descanso
        try:
            nuevo_descanso = input("¿Cuántos minutos quieres descansar? ")
            nuevo_descanso = int(nuevo_descanso)
            
            if nuevo_descanso > 0:
                tiempo_descanso = nuevo_descanso
                print(f"✅ Tiempo de descanso: {tiempo_descanso} minutos")
            else:
                print("❌ El tiempo debe ser mayor que 0")
                
        except ValueError:
            print("❌ Debes escribir un número")
    
    # ==================================
    # OPCIÓN 2: Empezar a estudiar
    # ==================================
    elif opcion == "2":
        if estado == "estudiando":
            print("\n⚠️  Ya estás estudiando")
            print("Termina el bloque actual primero (opción 3)")
        elif estado == "descansando":
            print("\n⚠️  Estás descansando")
            print("Termina el descanso primero (opción 3)")
        else:
            estado = "estudiando"
            print(f"\n📚 ¡A ESTUDIAR! ({tiempo_estudio} minutos)")
            print("Concéntrate y evita distracciones")
            print("Cuando termines, usa la opción 3")
    
    # ==================================
    # OPCIÓN 3: Terminar actividad
    # ==================================
    elif opcion == "3":
        if estado == "estudiando":
            # Terminamos de estudiar
            bloques_completados = bloques_completados + 1
            estado = "descansando"
            print(f"\n✅ ¡Bloque de estudio terminado!")
            print(f"Llevas {bloques_completados} bloques hoy")
            print(f"☕ HORA DE DESCANSAR ({tiempo_descanso} minutos)")
            print("Levántate, estira, toma agua...")
            
        elif estado == "descansando":
            # Terminamos de descansar
            estado = "esperando"
            print("\n✅ Descanso terminado")
            print("¿Listo para otro bloque de estudio?")
            
        else:
            print("\n❌ No hay nada activo")
            print("Primero empieza a estudiar (opción 2)")
    
    # ==================================
    # OPCIÓN 4: Ver resumen
    # ==================================
    elif opcion == "4":
        print("\n--- TU PROGRESO HOY ---")
        print(f"⏱️  Configuración: {tiempo_estudio} min estudio + {tiempo_descanso} min descanso")
        print(f"📊 Bloques completados: {bloques_completados}")
        
        # Calcular tiempo total estudiado
        tiempo_total = bloques_completados * tiempo_estudio
        horas = tiempo_total // 60
        minutos = tiempo_total % 60
        
        if horas > 0:
            print(f"⏰ Tiempo total estudiado: {horas} horas y {minutos} minutos")
        else:
            print(f"⏰ Tiempo total estudiado: {minutos} minutos")
        
        # Dar un mensaje motivacional según los bloques
        if bloques_completados == 0:
            print("💪 ¡Anímate a empezar tu primer bloque!")
        elif bloques_completados < 4:
            print("👍 ¡Buen comienzo! Sigue así")
        else:
            print("🌟 ¡Excelente! Has estudiado mucho hoy")
            
        input("\nPresiona Enter para continuar...")
    
    # ==================================
    # OPCIÓN 5: Salir
    # ==================================
    elif opcion == "5":
        print("\n👋 ¡Hasta luego!")
        if bloques_completados > 0:
            print(f"Completaste {bloques_completados} bloques hoy. ¡Bien hecho!")
        print("Recuerda: la constancia es la clave del éxito")
        break
    
    # ==================================
    # Opción no válida
    # ==================================
    else:
        print("\n❌ Elige un número del 1 al 5")

# Fin del programa