#Tenemos 6 patos con vidas distinas. El jugador cuenta con 30 municiones para realizar disparos y cada pato tiene un nivel de vida.
#Usted debe crear una lista con 6 numeros aleatorios entre 1 y 6. Esto representa a cada pato con su nivel de vida.
#El jugador debe ingresar la posicion a la que desea disparar. Un disparo a un pato le resta 1 punto de su vida.
#Cuando el pato llegue a 0, este es eliminado.
#Se debe validar que el usuario de una posicion valida(entre 1 y 6) y que no le dispare a un pato eliminado.


import random
print('Bienvenido a Patos Locos')
print('Estos son los patos: ')

#Primero crearemos los patos y sus niveles. Usaremos random para que se creen listas aleatorias cada vez.
patos=[]
for i in range(6):
    patos.append(random.randrange(1,7))

#Defino la variable "municiones" y la lista "eliminados" para usarlos como las condiciones de mi while.
#El while dejara de funcionar si ya no hay municiones o si todos los patos han sido eliminados.
municiones=30
print(patos)
eliminados=[0,0,0,0,0,0]
while municiones!=0 and patos!=eliminados:

    #Dentro del while defino una validacion, para comprobar que el usuario este dando una posicion que exista, y que no le dispare a un pato eliminado.
    validacion=False
    while validacion==False:
        posicionesPosibles=[0,1,2,3,4,5]
        posicion=int(input("Ingrese una posicion a disparar: "))-1 #Le resto 1, recordar que en las listas la primera posicion no es 1, sino 0. El usuario ingresara un valor entre 1 y 6, mientras que las posiciones reales estan entre 0 y 5.
        if posicion not in posicionesPosibles:
            print('Esta posicion no existe. Ingrese una posicion valida')
        else:
            if patos[posicion]==0:
                print('Escoja otro pato. Este ya ha sido eliminado')
            #Una vez que compruebo que cumpla los 2 requerimientos, rompo el while con la validacion.
            else:
                validacion=True

    #Le resto 1 de vida al pato en la posicion dada.
    patos[posicion]+=-1
    #Y le resto una bala. Si no agrego esta resta, el juego seguira por siempre.
    municiones+=-1
    print("Tiros restantes:"+str(municiones))
    print(patos)
#El juego terminara cuando ya no existan municiones o cuando los 6 patos sean eliminados.
print("")
print('GAME OVER')