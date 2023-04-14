evaluar = """ título: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures."""

evaluar_list = evaluar.split('resumen:') 
title_list = evaluar_list[0].split() 
title_list.pop(0) 
body = evaluar_list[1].split('\n')
body_list = " ".join(body).split('.') 
body_list = body_list[:-1]
cant_pray = {'facil': 0, 'aceptable': 0, 'dificil': 0,'muy_dificil':0} 
for prayer in body_list:
    match len(prayer.split()):
        case lenght if lenght < 13: cant_pray['facil'] += 1
        case lenght if 12 < lenght < 18: cant_pray['aceptable'] += 1
        case lenght if 17 < lenght < 26: cant_pray['dificil'] += 1
        case lenght if lenght > 25: cant_pray['muy_dificil'] += 1
if len(title_list) < 11:
    print('Titulo: ok')
else:
    print('Titulo: Sobre pasa las 10 palabras')
print(f"Cantidad de oraciones faciles de leer {cant_pray['facil']}, aceptables para leer: {cant_pray['aceptable']}, dificil de leer {cant_pray['dificil']}, muy dificiles de leer {cant_pray['muy_dificil']}")
