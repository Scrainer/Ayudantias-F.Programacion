def calcularBonos(listaEmpleados):
    listaBonos=[]
    for tupla in listaEmpleados:
        nombre,añosTrabajo,edad=tupla
        bono=(300*añosTrabajo)/100
        listaBonos=listaBonos+[(nombre,bono,edad)]
    return listaBonos


def calcularMáximoMinimo(listaBonos):
    maximoBono = 0
    empleadoMaximoBono = ""
    edadEmpleadoMaxi = 0

    minimoBono = 1000000000
    empleadoMinimoBono = ""
    edadEmpleadoMini = 0

    for tupla in listaBonos:
        nombre, bono, edad = tupla
        if bono > maximoBono:
            maximoBono = bono
            empleadoMaximoBono = nombre
            edadEmpleadoMaxi = edad
        if bono < minimoBono:
            minimoBono = bono
            empleadoMinimoBono = nombre
            edadEmpleadoMini = edad

    return (empleadoMaximoBono, edadEmpleadoMaxi, maximoBono), (empleadoMinimoBono, edadEmpleadoMini, minimoBono)


opcion = ""
while (opcion != "3"):
    print(".:Bienvenidos al menú de Consultas:.")
    print("1. Calcular y consultar bonos")
    print("2. Consultar datos del empleado con mayor y menor bono")
    print("3. Salir")
    print("-o-" * 10)
    opcion = input("Ingrese una opción: ")
    print("-o-" * 10)

    listaEmpleados = [("Juan", 6, 38), ("Andrea", 7, 36),
                      ("Anthonio", 8, 45), ("Ignacio", 9, 50), ("Simon", 10, 45)]
    listaBonos = calcularBonos(listaEmpleados)

    if opcion == "1":
        print("")
        for bonos in listaBonos:
            (nombre, bono, edad) = bonos
            print("-Nombre: " + nombre + ", -Bono: " + str(bono) +
                  ", -Edad: " + str(edad))
        print("")

    elif opcion == "2":
        empleadoMaximo, empleadoMinimo = calcularMáximoMinimo(listaBonos)
        print("\n.:Datos del empleado con mayor bono:.")
        print("\t*Nombre: " + empleadoMaximo[0] + "\n\t*Edad:"
              + str(empleadoMaximo[1]) + "\n\t*Bono: " + str(empleadoMaximo[2]) + "\n")
        print("\n.:Datos del empleado con menor bono:.")
        print("\t*Nombre: " + empleadoMinimo[0] + "\n\t*Edad:"
              + str(empleadoMinimo[1]) + "\n\t*Bono: " + str(empleadoMinimo[2]) + "\n")


    elif opcion == "3":
        print("\nGracias por su visita..!!")
    else:
        print("\nOpción incorrecta\n")