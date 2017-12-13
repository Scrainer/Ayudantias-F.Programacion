#Creador de listas
def crea_lista(contador):
    print("Dígame cuántas palabras tiene la lista", str(contador) + ": ", end="")
    numero = int(input())
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    return lista

print("Generador de listas")
numero = int(input("¿Cuántas listas quiere escribir? "))

listas = []
for i in range(1, numero + 1):
    listas += [crea_lista(i)]

for i in range(numero):
    print("La lista", i + 1, "es:", listas[i])

#Creador de Rectangulos
def rectangulo(ancho, alto, letra):
    for i in range(alto):
        for j in range(ancho):
            print(letra, end=" ")
        print()

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
caracter = input("Carácter a utilizar: ")
rectangulo(anchura, altura, caracter)

#Años Bisiestos
def es_bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)

print("Comprobador de años bisiestos")
fecha = int(input("Escriba un año y le diré si es bisiesto: "))
if es_bisiesto(fecha):
    print("El año", fecha, "es un año bisiesto.")
else:
    print("El año", fecha, "no es un año bisiesto.")