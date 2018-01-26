import numpy as np
#Ejercicio 1
def cargarArchivo(nombre):
    d={}
    fila=0
    archivo=open(nombre)
    for linea in archivo:
        palabras=linea.strip().split(" ")
        for i in range(len(palabras)):
            palabras[i]=palabras[i].strip().lower()
        d[fila]=palabras
        fila+=1
    archivo.close()
    matriz=np.empty((len(d),30),dtype="<U20")
    for linea,palabras in d.items():
        for i in range(len(palabras)):
            matriz[linea,i]=palabras[i]
    return matriz

#Ejercicio 2
def ocurrencias(palabra,matriz):
    return matriz[matriz==palabra].shape[0]
#Ejercicio 3
def lineas(palabra,matriz):
    filas=np.where(matriz==palabra)[0]
    filas+=1
    return tuple(filas)
#PPrincipal
arreglo=cargarArchivo('f.txt')
print(arreglo)
ocur=ocurrencias("amigos",arreglo)
print(ocur)
print(lineas("anillo",arreglo))