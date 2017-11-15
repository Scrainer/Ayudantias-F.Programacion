import numpy as np
altura = [180,215,210,210,188,176,209,200,210,188,176,209,200]
peso = [69,74,72,75,68,70,71,73,69,74,72,75,68,70,71,73]

np_altura=np.array(altura[:10])
np_peso=np.array(peso[:10])

np_altura_m=np_altura/100

print("Las alturas ingresadas en [m] son: ",np_altura_m)
print("Los pesos en [kg] son: ",np_peso)
print("\n")

imc=np_peso/(np_altura_m**2)
print("El arreglo de IMC es:")
print(imc)
print("\n")

for i in range(len(imc)):
    print("El  jugador ",i+1," tiene un IMC DE %6.2f"%imc[i])
a=imc[imc<16]
print("El valor del IMC que cumple con la condicion es %.2f"%a)
print("\n")

print("Determinar a que jugador le corresponde el IMC mas bajo")
lista1=[]
for i in range(len(imc)):
    if imc[i]<16:
        lista1.append(i+1)
for i in range(len(a)):
    print("El jugador ",lista1[i],"con IMC de %6.2f"%a[i],"debe presentarse a consulta medica")
print("\n")

print("El IMC mas alto se encuentra en la posicion:",np.argmax(imc),"y lo tiene el jugador",np.argmax(imc)+1)
print("\n")

promedio=np.sum(imc)/len(imc)
print("El promedio del IMC de los jugadores es: %6.2f"%promedio)