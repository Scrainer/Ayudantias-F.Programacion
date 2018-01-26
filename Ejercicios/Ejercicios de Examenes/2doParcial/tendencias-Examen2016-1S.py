tendencias={"08-22-2016":{"#Rio2016","#BSC","#ECU"},"08-25-2016":{"#GYE","#BRA"},"08-27-2016":{"#YoSoyEspol","#GYE","#BSC"}}
#Ejercicio A
def cuentaEtiquetas(diccionario,lista):
    conteo=dict()
    for fecha in lista:
        etiquetas=diccionario.get(fecha,"")
        if etiquetas!= "":
            for etiqueta in etiquetas:
                if etiqueta not in conteo:
                    conteo[etiqueta]=0
                conteo[etiqueta]+=1
    return conteo

#Ejercicio B
def reportaTendencias(diccionario,lista):
    todas=[]
    almenos=[]
    conteo=cuentaEtiquetas(diccionario,lista)
    for (etiqueta,conteo) in conteo.items():
        if conteo==len(lista):
            todas.append(etiqueta)
        if conteo >=1:
            almenos.append(etiqueta)
    if len(todas)==0:
        print("No hubo una etiqueta en comun en tendecia durante estos dias.")
    else:
        print("Esta(s) etiqueta(s) estuvieron en tendencia todos los dias:")
        print(todas)
    print("Esta(s) etiqueta(s) estuvieron en tendencia al menos un dia:")
    print(almenos)
    return

#Ejercicio C
def tendenciasExcluyentes(diccionario,fecha1,fecha2):
    etiquetasf1=diccionario[fecha1]
    etiquetasf2=diccionario[fecha2]
    excluidas=etiquetasf1.symmetric_difference(etiquetasf2)
    if len(excluidas)==0:
        print("No hay etiquetas para mostrar")
    else:
        print(excluidas)

#Programa Principal
print(cuentaEtiquetas(tendencias,["08-22-2016","08-25-2016","08-27-2016"]))
reportaTendencias(tendencias,["08-22-2016","08-27-2016"])
tendenciasExcluyentes(tendencias,"08-22-2016","08-27-2016")