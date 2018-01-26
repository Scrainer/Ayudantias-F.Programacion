#Ejercicio A
def buscar(listaAnidada,valor):
    for lista in listaAnidada:
        for elemento in lista:
            if elemento==valor:
                return True
    return False

#Ejercico B
L = [[3, 2, 5], [1], [7, 9]]
X = int(input("Ingrese valor por teclado: "))

if buscar(L, X):
    print("Valor sí existe")
else:
    print("Valor no existe")

# Literal c
def operarLista(listaAnidada, operacion="sumar"):
    resultado = 0
    if operacion == "multiplicar":
        resultado = 1
        for fila in listaAnidada:
            for celda in fila:
                if operacion == "sumar":
                    resultado += celda
                elif operacion == "multiplicar":
                    resultado *= celda
    return resultado