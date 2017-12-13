import miLibreriaAhorcado as m

vidas = 5
letrasAdivinadas = []
listaPalabras = ["manzana","pera","limon","uva"]
palabra = m.generarPalabra(listaPalabras)
#print(palabra)
m.presentarLetrasGuiones(palabra )

while vidas > 0:
    print("vidas:",vidas,"\tletras Adivinadas", letrasAdivinadas)
    letra = input("\nIngrese la letra:")

    if letra not in letrasAdivinadas:
        letrasAdivinadas.append(letra)

        if letra in palabra:
            m.presentarLetrasGuiones(palabra,letrasAdivinadas)

            if m.verificarSiGano(palabra, letrasAdivinadas) :
                print("Gano")
                break
        else:
            print("Letra no está en la palabra :( ")
            vidas -= 1
    else:
         print("Ya dijo la letra anteriormente")

if vidas == 0:
    print("Perdió")