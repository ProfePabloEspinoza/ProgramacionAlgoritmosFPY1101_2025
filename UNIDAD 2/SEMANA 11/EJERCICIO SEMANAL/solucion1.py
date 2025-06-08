"""
PROGRAMA: Control de Hidratación Diaria
OBJETIVO: Ayudar a controlar cuánta agua bebemos cada día
CONCEPTOS QUE APRENDEREMOS:
- Variables (para guardar información)
- Bucle while (para repetir el menú)
- Condicionales if/elif/else (para las opciones)
- Manejo de errores con try/except
"""

# ==================================
# PASO 1: Crear las variables
# ==================================
# Variables para guardar la información
meta_agua = 0.0           # Cuánta agua queremos beber (en mililitros)
agua_bebida = 0.0         # Cuánta agua hemos bebido hoy
tengo_meta = False        # ¿Ya decidimos nuestra meta? (Verdadero o Falso)

# Mensaje de bienvenida
print("🌊 ¡Bienvenido al Control de Hidratación! 🌊")
print("Este programa te ayuda a beber suficiente agua cada día")
print("Recuerda: Los adultos deben beber 2-3 litros diarios (2000-3000 ml)")

# ==================================
# PASO 2: Bucle principal del programa
# ==================================
# El programa seguirá funcionando hasta que elijamos salir
while True:
    # Mostrar información actual
    print("\n" + "-"*50)
    print("ESTADO ACTUAL:")
    
    if tengo_meta == True:
        print(f"🎯 Mi meta: {meta_agua} ml")
        print(f"💧 He bebido: {agua_bebida} ml")
        # Calcular y mostrar el porcentaje
        porcentaje = (agua_bebida / meta_agua) * 100
        print(f"📊 Progreso: {porcentaje:.0f}%")
    else:
        print("⚠️  Todavía no has establecido una meta")
    
    # Mostrar el menú
    print("\n¿QUÉ QUIERES HACER?")
    print("1. Establecer mi meta de agua para hoy")
    print("2. Registrar agua que bebí")
    print("3. Ver mi progreso detallado")
    print("4. Empezar un nuevo día (borrar todo)")
    print("5. Salir del programa")
    print("-"*50)
    
    # Pedir al usuario que elija una opción
    opcion = input("Elige una opción (1-5): ")
    
    # ==================================
    # OPCIÓN 1: Establecer la meta
    # ==================================
    if opcion == "1":
        print("\n--- ESTABLECER META ---")
        print("¿Cuánta agua quieres beber hoy?")
        print("Ejemplos: 2000 ml = 2 litros = 8 vasos aprox.")
        
        # Intentar leer un número
        try:
            entrada = input("Escribe tu meta en ml: ")
            meta_agua = float(entrada)
            
            # Verificar que sea un número positivo
            if meta_agua <= 0:
                print("❌ Error: La meta debe ser mayor que cero")
            else:
                tengo_meta = True
                print(f"✅ ¡Perfecto! Tu meta es beber {meta_agua} ml hoy")
                
        except ValueError:
            print("❌ Error: Debes escribir un número")
    
    # ==================================
    # OPCIÓN 2: Registrar agua bebida
    # ==================================
    elif opcion == "2":
        # Primero verificar si hay una meta
        if tengo_meta == False:
            print("\n❌ Primero debes establecer una meta (opción 1)")
        else:
            print("\n--- REGISTRAR AGUA ---")
            print("¿Cuánta agua acabas de beber?")
            print("Un vaso normal = 250 ml aprox.")
            print("Una botella pequeña = 500 ml aprox.")
            
            try:
                entrada = input("Cantidad en ml: ")
                cantidad = float(entrada)
                
                if cantidad <= 0:
                    print("❌ Error: La cantidad debe ser mayor que cero")
                else:
                    # Sumar a lo que ya habíamos bebido
                    agua_bebida = agua_bebida + cantidad
                    print(f"✅ Registrado: bebiste {cantidad} ml")
                    print(f"   Total del día: {agua_bebida} ml")
                    
                    # Dar feedback si alcanzó la meta
                    if agua_bebida >= meta_agua:
                        print("🎉 ¡FELICIDADES! ¡Alcanzaste tu meta!")
                        
            except ValueError:
                print("❌ Error: Debes escribir un número")
    
    # ==================================
    # OPCIÓN 3: Ver progreso detallado
    # ==================================
    elif opcion == "3":
        print("\n--- TU PROGRESO HOY ---")
        
        if tengo_meta == False:
            print("❌ Primero debes establecer una meta")
        else:
            print(f"🎯 Tu meta: {meta_agua} ml")
            print(f"💧 Has bebido: {agua_bebida} ml")
            
            # Calcular cuánto falta
            falta = meta_agua - agua_bebida
            
            if agua_bebida >= meta_agua:
                extra = agua_bebida - meta_agua
                print(f"🎉 ¡Meta cumplida! Bebiste {extra} ml extra")
            else:
                print(f"📈 Te faltan: {falta} ml")
                # Convertir a vasos para que sea más fácil de entender
                vasos = falta / 250
                print(f"💡 Eso es aproximadamente {vasos:.1f} vasos")
                
        input("\nPresiona Enter para continuar...")
    
    # ==================================
    # OPCIÓN 4: Nuevo día (reiniciar)
    # ==================================
    elif opcion == "4":
        print("\n--- NUEVO DÍA ---")
        confirmacion = input("¿Seguro que quieres borrar todo? (s/n): ")
        
        if confirmacion.lower() == "s":
            # Reiniciar todas las variables
            meta_agua = 0.0
            agua_bebida = 0.0
            tengo_meta = False
            print("✅ Todo reiniciado. ¡Comienza un nuevo día!")
        else:
            print("Cancelado. No se borró nada.")
    
    # ==================================
    # OPCIÓN 5: Salir
    # ==================================
    elif opcion == "5":
        print("\n👋 ¡Hasta luego! Recuerda mantenerte hidratado 💧")
        break  # Esta instrucción termina el bucle while
    
    # ==================================
    # Si escribió algo que no es 1-5
    # ==================================
    else:
        print("\n❌ Opción no válida. Escribe un número del 1 al 5")

# Fin del programa
print("Programa terminado")