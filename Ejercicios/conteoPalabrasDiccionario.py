diccionario={}
for repeticion in range(10):
    palabra=input("Ingrese una palabra: ")
    if palabra in diccionario:
        diccionario[palabra]+=1
    else:
        diccionario[palabra]=1
print(diccionario)