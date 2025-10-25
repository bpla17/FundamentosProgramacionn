# Programa: Museo de Antropología e Historia

print("Bienvenido al Museo de Antropología e Historia")
print("==============================================")

total = 0  # acumulador del total a pagar

while True:
    edad = int(input("\nIngresa la edad del visitante (0 para salir): "))
    if edad == 0:
        print("Fin del registro de visitantes.")
        break  # sale del ciclo si el usuario escribe 0

    if edad < 3:
        print("El visitante no paga boleto.")
        continue  # pasa al siguiente visitante sin cobrar

    # Determinar precio base según edad
    if edad < 18:
        precio = 30
    else:
        precio = 45

    # Tipo de visitante y descuento
    print("Tipo de visitante:")
    print("1. Adulto mayor (12%)")
    print("2. Profesor (10%)")
    print("3. Estudiante (10%)")
    print("4. Ninguno")
    tipo = int(input("Selecciona una opción: "))

    if tipo == 1:
        descuento = 0.12
    elif tipo == 2 or tipo == 3:
        descuento = 0.10
    else:
        descuento = 0.0

    # Calcular precio final
    precio_final = precio * (1 - descuento)
    print(f"Precio a pagar por este visitante: ${precio_final:.2f}")

    # Acumular total
    total += precio_final

print(f"\nEl total a pagar por todos los visitantes es: ${total:.2f}")
