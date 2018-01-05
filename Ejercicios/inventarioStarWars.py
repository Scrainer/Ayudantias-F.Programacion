reporte=["C3PO|Droides|Protocolo",
"Halcon Milenario|Naves|Carga",
"R2D2|Droides|Astromecanico",
"BB8|Droides|Astromecanico",
"DH17,2|Armas|Desintegrador",
"A280,1|Armas|Desintegrador"]
dicc={}
for linea in reporte:
    datos=linea.split("|")
    if datos[1] not in dicc:
        if "," in datos[0]:
            lista=datos[0].split(",")
            dicc[datos[1]]={datos[2]:[(lista[0],int(lista[1]))]}
        else:
            dicc[datos[1]]={datos[2]:[datos[0]]}
    else:
        if "," in datos[0]:
            lista = datos[0].split(",")
            if datos[2] not in dicc[datos[1]]:
                dicc[datos[1]][datos[2]]=[(lista[0],int(lista[1]))]
            else:
                dicc[datos[1]][datos[2]].append((lista[0],int(lista[1])))
        else:
            if datos[2] not in dicc[datos[1]]:
                dicc[datos[1]][datos[2]]=[datos[0]]
            else:
                dicc[datos[1]][datos[2]].append(datos[0])
print(dicc)