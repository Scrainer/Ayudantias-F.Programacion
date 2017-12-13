def estudiantesUnaMateria(lista1, lista2):
    matriculasUna = []
    for matricula in lista1:
        matriculasUna.append(matricula)
    for matricula2 in lista2:
        if matricula2 not in matriculasUna:
            matriculasUna.append(matricula2)
        elif matricula2 in matriculasUna:
            matriculasUna.remove(matricula2)
    return matriculasUna


listaFund = ["201606710", "201336710", "201006720", "201456710", "200345671"]
listaBio = ['201606710', '201056723', '201231710', '201456710', '201336710']
print(listaFund)
print(listaBio)
listaUna = estudiantesUnaMateria(listaFund, listaBio)
print(listaUna)
