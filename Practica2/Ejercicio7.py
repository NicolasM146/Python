texto = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que 
el de una mujer es de $45.000. Además, las mujeres tienen menos 
posibilidades de acceder a puestos de liderazgo en las empresas.
 """
palabras=len(texto.split())
mayusculas=[letras for letras in texto if letras.isupper()]
minusculas=[letras for letras in texto if letras.islower()]
noLetras=[letras for letras in texto if not letras.isalpha() and not letras.isspace()]

print("Mayusculas ",mayusculas)
print("Minusculas ",minusculas)
print("No Letras",noLetras)
print("Cantidad de palabras",palabras)
