datos=["cuenca,temperatura,22","guayaquil, precio,13000","cuenca,precio,120000","guayaquil,temperatura,29"]
dic=dict()

for info in datos:
    lista=info.split(",")
    ciudad=lista[0]
    infoex=lista[1]
    valor = lista[2]
    if ciudad not in dic:
        dic[ciudad]=dict()
        dic[ciudad][infoex]=valor
    else:
        dic[ciudad][infoex] = valor

print(dic)
