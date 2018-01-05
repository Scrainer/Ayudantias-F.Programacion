days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

print("Literal a")
mes=input("Ingrese un mes: ").capitalize()

if mes in days:
   print("El mes %s tiene %d días"%(mes,days[mes]))
else:
   print("El mes no se encuentra en el diccionario")

print("\nLiteral b")

claves_ordenadas=sorted(days)

print("Claves en orden alfabético: ")

for clave in claves_ordenadas:
   print(clave)

print("\nLiteral c")
print("Los meses con 31 días son: ")

for clave in days:
   if days[clave]==31:
       print(clave)

print("\nLiteral d")
clave_or_val=sorted(days,key=days.get)

for clave in clave_or_val:
   print((clave,days[clave]))