def media(matriz):
    contador=0
    suma=0
    for i in range(0,len(matriz[:,0])):
        for j in range(0,len(matriz[0,:])):
            suma+=matriz[i,j]
            contador+=1
    return (suma/contador)
def numMayores(matriz):
    cantidad=0
    promedio=media(matriz)
    for i in range(0,len(matriz[:,0])):
        for j in range(0,len(matriz[0,:])):
            if matriz[i,j]>promedio:
                cantidad+=1
    return cantidad
def numMenores(matriz):
    cantidad = 0
    promedio = media(matriz)
    for i in range(0, len(matriz[:, 0])):
        for j in range(0, len(matriz[0, :])):
            if matriz[i, j] < promedio:
                cantidad += 1
    return cantidad

import numpy as np
m=np.array([[1,2,3,4],
            [2,3,4,5],
            [3,4,5,6]])
print(m)
print(media(m))
print(numMayores(m))