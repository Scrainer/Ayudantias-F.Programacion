import numpy as np
import math
lista = ['112|CampoBolivar|0-2|97', '116|CampoZamora|3-0|86', '117|CampoTungurahua|4-3|101', '119|CampoPastaza|2-1|78']

def generarMatriz(lista):
    matriz = np.zeros((5,5), dtype=int) # Genera la matriz del tamaño minimo posible considerando la lista.
    for campo in lista:
        coord = campo.split('|')[2].split('-')  # coord = tupla con la coordenada del campo ej. coord = (0,2)
        matriz[int(coord[0]), int(coord[1])] = lista.index(campo) + 1   # Sustituye la coordenada con el índice mas 1.
                                                                        #  le añade uno para que el indice 0 no se pierda en la matriz np.zeros
    return matriz

def reporteArea(matriz, lista, pInicio, pFinal): # pInicio/pFinal = coordenadas de la forma (x,y)
    seleccion = matriz[pInicio[0]:pFinal[0]+1, pInicio[1]:pFinal[1]+1]  # Recorta la matriz en las coordenadas ingresadas, tomando en cuenta
                                                                        # que a la coordenada final se le debe sumar uno.
    print(seleccion)
    barriles = 0    # Contador de barriles totales seleccionados en el area
    for item in seleccion[np.where(seleccion != 0)]:    # np.where devuelve una tupla con los índices donde se cumple la condición.
                                                        # Se indexa la misma seleccion para extraer los items que cumplen la condición
        barriles += int(lista[item-1].split('|')[-1])   # Los items que cumplen la condición son nada más que el índice del campo
                                                        # de la lista menos 1.
    return barriles

matriz = generarMatriz(lista)
print(matriz)
print(reporteArea(matriz, lista, (0,0), (4,4)))
