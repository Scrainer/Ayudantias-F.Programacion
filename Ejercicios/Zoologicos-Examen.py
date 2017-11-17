import numpy as np
#Datos
animales_felinos=[...]
animales_simios=[...]
zoologicos_costa=[...]
zoologicos_sierra=[...]
zoologicos_oriente=[...]
tipos_comida=[...]
#Matrices
datos_zoo=np.array([...])
alimentos=np.array([...])

#A Dererminar el total de alimentos en el sistema de zoologicos
total=datos_zoo.sum()

#B El total de kg de comida que necesitan los animales por tipo de comida
total_animales=datos_zoo.sum(axis=0)
for i in range(len(tipos_comida)):
    total_tipo=alimentos[i,:]*total_animales
    suma_total_tipo=total_tipo.sum()
    print("Se necesita",suma_total_tipo,"kg de",tipos_comida[i],"para todos los zoos")

#C Determinar el zoologico con mayor numero de animales (nombre)
totalanimales_por_zoo=datos_zoo.sum(axis=1)
maximo=totalanimales_por_zoo.max()
indicemaximo=totalanimales_por_zoo.argmax()
todos_zoo=zoologicos_costa+zoologicos_sierra+zoologicos_oriente
zoo_max=todos_zoo[indicemaximo]
print("El zologico con mayor numero de animales es el",zoo_max,"con",maximo,"animales.")

#D Determinar el animal con mayor presencia en los zoologicos del pais
presencia=total_animales.max()
indicepresencia=total_animales.argmax()
todos_animales=animales_felinos+animales_simios
animal_presencia=todos_animales[indicepresencia]
print("El animal con mayor presencia es el",animal_presencia,"con",presencia,"ejemplares.")

#Determinar el presupuesto de comida para zoologicos de costa y sierra
total_animalesCostaSierra=datos_zoo[:len(zoologicos_costa+zoologicos_sierra),:].sum(axis=0)
presupuesto=0
for i in range(len(tipos_comida)):
    total_por_tipo=total_animalesCostaSierra*alimentos[i,:]
    costo=total_por_tipo*3
    presupuesto+=costo.sum()
print(presupuesto)