palabra = input("Ingresá una palabra: ")
if "a" in palabra and "n" in palabra:
    print("Hay letras a y n")
elif "a" in palabra:
    print("Solo tiene letra a, pero no n")
elif "n" in palabra:
    print("Solo tiene letra n, pero no a")
else:
    print("No hay letras a y n ")