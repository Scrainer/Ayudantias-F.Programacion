#Ejercicio 1
def academico(archivos):
    notas1,notas2=archivos
    notas=dict()
    archivo1=open(notas1)
    archivo2=open(notas2)
    for linea in archivo1:
        datos=linea.strip().split(",")
        matricula=datos[0]
        materia=datos[1]
        notaParcial=datos[2]
        notaFinal=datos[3]
        notaMejoramiento=datos[4]
        estado=datos[5]
        tupla=(materia,notaParcial,notaFinal,notaMejoramiento,estado)
        if matricula not in notas:
            notas[matricula]={notas1:[]}
        notas[matricula][notas].append(tupla)