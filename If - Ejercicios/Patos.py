#Tenemos 6 patos con vidas distinas
import random
lista=[]
for i in range(6):
    lista.append(random.randrange(1,7))
municiones=30
print(lista)
while municiones!=0:
    validacion=False
    while validacion==False:
        posicionesPosibles=[0,1,2,3,4,5]
        posicion=int(input("Ingrese una posicion a disparar: "))
        if posicion not in posicionesPosibles:
            print('Esta mal')
        else:
            if lista[posicion]==0:
                print('Escoja otro pato. Este ya esta muerto')
            else:
                validacion=True
    lista[posicion]=lista[posicion]-1
    municiones+=-1
    print("Tiros restantes:"+str(municiones))
    print(lista)
print("Termino el juego")