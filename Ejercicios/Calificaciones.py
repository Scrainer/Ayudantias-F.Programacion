list = []

cont = 1
while cont == 1:
    alumno = input("Nombre del alumno: ")
    calificaciones=[]
    notas=input("Ingrese notas ")
    calificaciones=notas.split(",")
    for i in range(len(calificaciones)):
        calificaciones[i]=float(calificaciones[i])
    prom=sum(calificaciones)/len(calificaciones)
    print(prom)
    if prom >= 6.0:
        a = "Aprobado"
        print(a)
    else:
        b = "Desaprobado"
        print(b)
    cont = int(input("¿Seguir calificando? 1-Yes 2-No: "))

for i in list:
    print(i + " : " + str(list[i]))
