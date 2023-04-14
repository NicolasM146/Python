nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín', 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def juntar(nombres,notas_1,notas_2):
    dicc = dict(zip(nombres, map(lambda x, y: (x, y), notas_1, notas_2)))
    return dicc

def promedios(dicc):
    promAlum={}
    for clave,valor in dicc.items():
        promAlum[clave]=sum(valor)/len(valor)
    return promAlum
        
def promedioGeneral(dicc):
    promedios = {} 
    for nombre, notas in dicc.items():   
                
        promedio = sum(notas) / len(notas) 
        promedios[nombre]  = promedio 
    return promedios

def NotaPromMasAlta(promAlum):
    maximo=0
    for clave,valor in promAlum.items():
        if(valor > maximo):
            alumno=clave
            maximo=valor
    return maximo,alumno
        
def NotaMasBaja(dicc):
    menor=999
    for clave,valor in dicc.items():
        menorV=min(valor)
        if(menorV < menor):
            alumno=clave
            menor=menorV
    return menor,alumno
    



nombres = nombres.replace("'", "").replace(" ", "").replace("\n","").split(",")
dicc=juntar(nombres,notas_1,notas_2)

print(dicc)

promAlum=promedios(dicc)
for clave,valor in promAlum.items():
    print("El promedio de",clave,"es",valor)

promedios=promedioGeneral(dicc)
prom= sum(promedios.values())/len(nombres)
print("El Promedio General es",prom)

maxP,alumP=NotaPromMasAlta(promAlum)
print("El promedio mas grande es de",alumP,"con",maxP)

menor,alumno=NotaMasBaja(dicc)
print("La notas mas baja es de",alumno,"con una nota de",menor)