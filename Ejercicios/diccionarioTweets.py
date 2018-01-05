tweets={1:{'geo_enabled': True, 'description':'Disfrutando de las vacaciones.', 'location': 'Guayaquil, Ecuador','user':{"id": 2244994945,'screen_name': 'elenajk'}},
2: {'geo_enabled': True, 'description':'Con mis amigas', 'location':'Quito, Ecuador','user':{"id": 6555194743,'screen_name': 'samirajs'}
},3: {'geo_enabled': True, 'description':'De viaje con mi familia por las vacaciones', 'location':'Guayaquil, Ecuador','user':{"id": 9276494798,'screen_name': 'mariomr'}
},4: {'geo_enabled': True, 'description':'Paseando por Manabí, mañana regreso', 'location':'Manabí, Ecuador','user':{"id": 8376984508,'screen_name': 'luisde'}
}}
palabras={'paseo','viaje','vacaciones','diversión','disfrutando','paseando','viajando', 'tour'}

dic_ciudad={}
dic_usuario={}
for id,tweet in tweets.items():
       desc=tweet['description'].lower().split(" ")
       set(desc)
       interseccion=palabras.intersection(desc)
       cont=len(interseccion)
       if cont>=1:
           ciudad=tweet['location'].split(",")[0]
           dic_ciudad[ciudad]=dic_ciudad.get(ciudad,0)+1

           usuario=tweet['user']['screen_name']
           dic_usuario[ciudad]=dic_usuario.get(ciudad,[])+[usuario]
for ciudad, numero in dic_ciudad.items():
   print(ciudad,numero)
print()
for ciudad, lista_usu in dic_usuario.items():
   print(ciudad)
   cont=1
   for usu in lista_usu:
       print(cont,usu)
       cont+=1