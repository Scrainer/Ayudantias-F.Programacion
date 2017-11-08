import random
juego=True
recipientes=[0,0,0]

while juego==True:
    puntaje=random.randrange(0,10)
    validacion=False
    while validacion==False:
        posicionesposibles=[0,1,2]
        posicion=int(input('Ingrese una posicion: '))
        if posicion not in posicionesposibles:
            print('De una posicion correcta')
        else:
            validacion=True
    print("El puntaje aleatorio es: "+str(puntaje))
    recipientes[posicion]+=puntaje
    print(recipientes)
    if recipientes[0]>10 and recipientes[1]>10 and recipientes[2]>10:
        print('Ha ganado')
        juego=False