import numpy as np

def generarMatriz(listaMultas):
    multas = np.zeros((5, 5), int)
    for f,c,m in listaMultas:
        multas[f, c] += m
    return multas

def sectorTop(matriz):
    sectores = dict()
    sectores["Norte"] = matriz[0].sum()
    sectores["Sur"] = matriz[-1].sum()
    sectores["Oeste"] = matriz[1: -1, 0].sum()
    sectores["Este"] = matriz[1: -1, -1].sum()
    sectores["Centro"] = matriz[1: -1, 1: -1].sum()
    sectoresTop = sorted(sectores, key=sectores.get, reverse=True)
    return (sectoresTop[0],sectores[sectoresTop[0]])

# Prueba de funciones
listaMultas = [(0, 0, 120), (1, 2, 330), (3, 4, 123), (4, 2, 62), (0, 0, 50),(4, 4, 89), (0, 3, 25), (2, 0, 43), (3, 2, 21), (0, 0, 120)]

multas = generarMatriz(listaMultas)
print("\nMatriz de multas:\n\n{}\n".format(multas))

tuplaSectorTop = sectorTop(multas)
print("Sector Top:\n\n{}\n".format(tuplaSectorTop))