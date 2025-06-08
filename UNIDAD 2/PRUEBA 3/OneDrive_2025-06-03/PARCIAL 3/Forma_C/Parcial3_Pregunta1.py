while True:
    try:
        cant = int(input("Ingrese la cantidad de pacientes atendidos: "))
        break
    except:
        print("Debe ingresar un número entero.")

pacientes_mas_de_2_tratamientos = 0

for i in range(cant):
    while True:
        try:
            tratamientos = int(input("Ingrese la cantidad de tratamientos realizados: "))
            break
        except:
            print("Debe ingresar un número entero.")
    if tratamientos > 2:
        print("Paciente con más de 2 tratamientos.")
        pacientes_mas_de_2_tratamientos += 1
    else:
        print("Paciente con 2 o menos tratamientos.")

print(f"Se registraron {pacientes_mas_de_2_tratamientos} pacientes con más de 2 tratamientos.")
print(f"Se registraron {cant - pacientes_mas_de_2_tratamientos} pacientes con 2 o menos tratamientos.")
