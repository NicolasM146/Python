clave1=["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
clave2=["D", "G"]
clave3=["B", "C", "M", "P"]
clave4=["F", "H", "V", "W", "Y"]
clave5=["K"]
clave6=["J", "X"]
clave7=["Q", "Z"]
dicc={tuple(clave1): 1,tuple(clave2):2,tuple(clave3):3,tuple(clave4):4,tuple(clave5):5,
      tuple(clave6):8,tuple(clave6):10}
palabra=input("Escribir una Palabra: ")
cant=0
for elem in palabra:
    for clave, valor in dicc.items():
        if elem.upper() in clave:
            cant+=valor
print("La cantidad de Puntos es: ", cant)