texto = input("Ingrese una palabra o frase: ")


texto = [letra for letra in texto if letra.isalpha()]

if len(texto) == len(set(texto)):
    print("La palabra o frase ingresada es un Heterograma.")
else:
    print("La palabra o frase ingresada no es un Heterograma.")
