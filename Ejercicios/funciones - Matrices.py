def media(matriz):
    contador=0
    suma=0
    for i in range(0,len(matriz[:,0])):
        for j in range(0,len(matriz[0,:])):
            suma+=matriz[i,j]
            contador+=1
    return (suma/contador)

import numpy as np
m=np.array([[1,2,3,4],
            [2,3,4,5],
            [3,4,5,6]])
print(media(m))