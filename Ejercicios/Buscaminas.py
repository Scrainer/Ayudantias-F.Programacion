import random
juego=[0,0,0,0,0,0,0,0]
juego2=[0,0,0,0,0,0,0,0]
print('Bienvenido a buscaminas')
posicionesMina=[]
for i in range(3):
    posicionRandom=random.randrange(0,9)
    juego2[posicionRandom]=-1
