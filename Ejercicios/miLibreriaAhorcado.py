import random as r


def generarPalabra(listado):
    indice = r.randint(0, len(listado) - 1)
    return listado[indice]

def presentarLetrasGuiones( pal, letras = []):
    if len(letras) == 0:
        print("_ " * len(pal))
    else:
        for i in pal:
            if i in letras:
                print(i," ", end='')
            else:
                print("_"," ",end='')
        print("\n")

def verificarSiGano(palabraAdivinar, letras):

    for i in palabraAdivinar:
        if i not in letras:
            return False
    return True
