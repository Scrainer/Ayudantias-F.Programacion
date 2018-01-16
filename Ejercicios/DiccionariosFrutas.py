supermercado=[("banana",4,6),("manzana",2,0),("naranja",1.5,32),("pera",3,15)]

precios=dict()
stock=dict()

for (c,p,s) in supermercado:
    precios[c]=p
    stock[c]=s
print(precios)
print(stock)

total=0
for comida in precios:
    print(comida)
    print("precio: %s" % precios[comida])
    print("stock: %s" % stock[comida])
    dinero=precios[comida]*stock[comida]
    total+=dinero
    print()

print("El costo total es:", total)
