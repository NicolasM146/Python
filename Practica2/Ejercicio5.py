pa=input("Escribir una palabra: ")
palabra= """Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo
tres tristes tigres."""
l=palabra.split()
cant=0
for elem in l:
    print(elem)
    if pa  in elem.lower() or pa in elem.upper() :
        cant+=1
print(f"Las veces que aparece [{pa}], son {cant}")