import string
letras = string.ascii_letters
jupyter_info = """ JupyterLab is a web-based interactive development 
environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user 
interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. 
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing 
ones."""
line =jupyter_info.split()
l = input("Leer una letra")
if l in letras:
    for elem in line:
        if elem.lower().startswith(l):
            print(f"{l} Se encuentra en {elem}")
else:
    print(f"{l} no es una letra")