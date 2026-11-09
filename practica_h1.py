# Inicializacion del contador, acumulador y extremos
contador = 0
suma = 0
mayor = 0
menor = 10

# Inicializacion de la opcion del menu
opcion = 0

# Repetir el menu hasta que el usuario elija salir
while opcion != 5:

    # Mostrar las opciones del menu
    print("\n--- MENU --")
    print("1. Introducir una nota")
    print("2. Ver numero de notas")
    print("3. Ver media")
    print("4. Ver nota mas alta y mas baja")
    print("5. Salir")

    # Pedir una opcion al usuario
    opcion = int(input("Elige una opcion: "))

    # Opcion 1: introducir y validar una nota
    if opcion == 1:
        nota = float(input("Introduce una nota: "))

        if nota >= 0 and nota <= 10:

            # Actualizar contador y acumulador
            contador += 1
            suma += nota

            # Inicializar los extremos con la primera nota
            if contador == 1:
                mayor = nota
                menor = nota

            # Actualizar la nota mas alta y la mas baja
            else:
                if nota > mayor:
                    mayor = nota

                if nota < menor:
                    menor = nota

        else:
            print("La nota debe estar entre 0 y 10")

    # Opcion 2: mostrar el numero de notas introducidas
    elif opcion == 2:
        print("Numero de notas:", contador)

    # Opcion 3: calcular y mostrar la media
    elif opcion == 3:
        if contador == 0:
            print("No hay notas introducidas")
        else:
            media = suma / contador
            print("La media es:", media)

    # Opcion 4: mostrar la nota mas alta y la mas baja
    elif opcion == 4:
        if contador == 0:
            print("No hay notas introducidas")
        else:
            print("Nota mas alta:", mayor)
            print("Nota mas baja:", menor)

    # Opcion 5: salir del programa
    elif opcion == 5:
        print("Saliendo del programa...")

    # Controlar las opciones que no existen
    else:
        print("Opcion no valida")
