#Elabore un juego que consistira en acumular puntos en 3 recipientes.
#Luego debe generar un numero aleatorio entre 0 y 9, que lo ira almacenando en uno de los recipientes seleccionados previamente.
#Cuando los recipientes acumulen mas de 10 puntos el juego terminara.
#Cada vez que genere un numero aleatorio, debe mostrarlo y mostrar el estado de los recipientes



import random

#Usamos un while y la variable "juego" para mantener el juego corriendo.
juego=True
recipientes=[0,0,0]

while juego==True:
    puntaje=random.randrange(0,10)

    #Usamos otro while para validar que el usuario nos de una posicion que este dentro del rango. Si la posicion dada es correcta, se rompe el bucle.
    validacion=False
    while validacion==False:
        posicion=int(input('Ingrese una posicion: '))
        if posicion not in range(0,3):
            print('De una posicion correcta')
        else:
            validacion=True

    print("El puntaje aleatorio es: "+str(puntaje))

    #Cambiamos el estado del recipiente.
    recipientes[posicion]+=puntaje
    print(recipientes)

    #Una vez que se cumpla la condicion, el bucle while original se rompe.
    if recipientes[0]>10 and recipientes[1]>10 and recipientes[2]>10:
        print('Ha ganado')
        juego=False