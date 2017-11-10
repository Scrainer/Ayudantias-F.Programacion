#Juego Buscaminas
#Se debe crear una lista con 8 ceros en la que colocara 3 minas aleatoriamente. (Las minas encontradas se representaran con un -1.
#El usuario tendra 5 intentos para encontras las 3 minas y marcarlas. Si el usuario las encuentra todas, mostrar que gano.
#Si se queda sin intentos y todavia tiene minas se mostrar que perdio.

import random
print("<<<BIENVENIDOS A BUSCAMINAS>>>")

#Primero creamos la lista en la que jugaremos
juego=[0,0,0,0,0,0,0,0]

#Luego yo creo una lista, donde pondremos las posiciones o index donde estaran las minas. Las 3 posiciones aleatorias las creo usando for y el random.
posicionesMina=[]
for i in range(3):
    posicionRandom=random.randrange(8)
    #Con este while me aseguro de que no haya posiciones repetidas.
    while posicionRandom in posicionesMina: #El while seguira creando numeros aleatorios hasta que encuentre uno que no este creado ya.
        posicionRandom=random.randrange(8)
    posicionesMina.append(posicionRandom) #Agrego la posicion a la lista que se creo antes.

#Establecemos 2 variables que serviran como nuestro contadores para el while que aplicaremos.
intentos=5
minas=3

#Al while le doy dos condiciones. El juego puede terminar cuando ya no haya intentos, o cuando ya se hayan encontrado todas las minas.
while intentos!=0 and minas!=0:
    print(juego)
    adivinanza=int(input("Ingrese una posicion: "))
    print()
    intentos+=-1 #Aqui aplicamos el primer contador para que cada vez que se de una posicion, los intentos disminuyan
    #Con el if verificaremos si verdaderamente el jugador le atino a una de las posiciones de las minas, si le dio a una mina, el 0 se reemplazara con el -1.
    #Si no le da a una mina, se le dira que fallo o si dio una posicion inexistente.
    if adivinanza in posicionesMina:
        juego[adivinanza]=-1
        print("Ha encontrado una mina. Le quedan "+str(intentos)+" intentos y "+str(minas)+" minas.")
        #Ponemos este contador dentro del if para que solo disminuya en el caso que haya encontrado una mina. Si este estubiera afuera, disminuiria la cantidad de minas sin importar si el jugador la encontro o no, cosa que no queremos que suceda.
        minas+=-1
    #Este elif verificara que la posicion este entre 0 y 8 y que no sea una mina.
    elif (adivinanza in range(len(juego))) and (adivinanza not in posicionesMina):
        print("No ha encontrado una mina. Le quedan "+str(intentos)+" intentos y "+str(minas)+" minas.")
    #Finalmente este else seran todos los numeros que no esten dentro del rango.
    else:
        print("Posicion no existente. Le quedan "+str(intentos)+" intentos y "+str(minas)+" minas.")

#Para imprimir si el jugador gano o no solo nos basamos en las minas. Si ya no hay minas, gano. Si aun hay apesar de no tener intentos, pierde.
#En este caso no consideramos la cantidad de intentos como condicion por que el usuario puede ganar bajo estos casos:
#1.Encontro todas las minas sin quedarse sin intentos
#2.Encontro todas las minas, encontrando la ultima mina con su ultimo intento.
#Como en ambos casos el valor de minas es igual a 0, podemos ignorar la condicion de los intentos.
#Si no tiene intentos y no encontro minas, el valor sera diferente de 0. Haciendo valer el else.
if minas==0:
    print("Felicidades ha ganado.")
else:
    print("Perdio. Vuelva a intentarlo.")