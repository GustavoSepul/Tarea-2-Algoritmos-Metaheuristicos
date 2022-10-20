import numpy as np
import pandas as pd
import sys 



# df = pd.read_csv('berlin52.txt', sep =" ", header = None)
# print(df)
# semilla 
# tamaño colonia
# numero iteraciones
# tasa de evaporacion
# factor de importancia euristica (2,5)
# probabilidad exploracion explotacion (0 - 1)
# archivo de entrada

if len(sys.argv) == 4:
    seed = int(sys.argv[1])
    h = int(sys.argv[2])
    archivo = str(sys.argv[3])
    print(seed, h, archivo)
else:
    sys.exit(0)


poblacion = np.full((h, 52), -1)
for i in range(h):
    poblacion[i][0] = np.random.randint(52)
print("Poblacion inicial :")
print(poblacion)

coordenadas = pd.read_table(archivo, header = None,delim_whitespace=True, skiprows=6, skipfooter=2, engine='python')
coordenadas = coordenadas.drop(columns =0,axis=1).to_numpy()
print("Matriz Coordenadas: ")
print(coordenadas)
cant_variables = coordenadas.shape[0]

distancias = np.full((cant_variables,cant_variables), fill_value=-1.0,dtype=float)
for i in range(cant_variables-1):
    for j in range(i+1,cant_variables):
        distancias[i][j] = np.sqrt(np.sum(np.square(coordenadas[i]-coordenadas[j])))
        distancias[j][i] = distancias[i][j]
print("Matriz Distancias: ")
print(distancias)

heuristica = np.full_like(distancias,fill_value=1/distancias, dtype=float)
np.fill_diagonal(heuristica,0)
print("Matriz Heuristica: ")
print(heuristica)


def Calcular_costo(n,s,c):
    aux = c[s[n-1]][s[0]]
    for i in range(n-1):
        aux += c[s[i]][s[i+1]]
    return aux




mejor_solucion = np.arange(0,cant_variables)
np.random.shuffle(mejor_solucion)
mejor_costo = Calcular_costo(cant_variables,mejor_solucion,distancias)
print(mejor_costo)


