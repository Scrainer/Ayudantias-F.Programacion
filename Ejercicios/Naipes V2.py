import random
naipes=[]
carta1=naipes.append(random.randint(1,13))
carta2=naipes.append(random.randint(1,13))
pregunta=0
while pregunta!='salir':
    print("Sus naipes son:", naipes)
    pregunta = input("Escoja una opcion:\n"
                     "a. Escoger otro naipe\n"
                     "b. Salir\n"
                     "Escriba la letra de su opción: ")
    if pregunta=='a':
        carta = naipes.append(random.randint(1, 13))
        print("Se le ha dado otro naipe")
    elif pregunta=='b':
        pregunta='salir'
print("Sus naipes al final de la partida son:",naipes)
    print("La suma de sus naipes es:",sum(naipes))
    if sum(naipes)>=20:
        print("Ganó el juego!")
    else:
        print("Ha perdido")
print("Game Over")