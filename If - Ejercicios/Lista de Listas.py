lista=[1,2,3,['a','b']]
lista2=[['Lambo','BMW'],['BarCOS','BOTES','LANCHAS']]

lista3=[]
for i in range(3):
    ingreso=input('Ingrese 2 letras')
    letras=ingreso.split(',')
    lista3.append(letras)
print(lista3)


