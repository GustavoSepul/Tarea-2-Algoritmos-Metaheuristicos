import numpy as np
import pandas as pd
import sys 


df = pd.read_table('berlin52.tsp', header = None,delim_whitespace=True, skiprows=6, skipfooter=2, engine='python')
df = df.drop(columns=0,axis=1).to_numpy()
print(df)
variables = df.shape[0]
print(variables)

if len(sys.argv) == 5:
    seed = int(sys.argv[1])
    h = int(sys.argv[2])
    itereaciones = int(sys.argv[3])
    archivo = str(sys.argv[4])
    print(seed, h, archivo)
else:
    sys.exit(0)

def Calcular_costo(n,s,c):
    aux = c[s[n-1]][s[0]]
    for i in range(n-1):
        aux += c[s[i]][s[i+1]]
    return aux

coordenadas = pd.read_table(archivo, header = None,delim_whitespace=True, skiprows=6, skipfooter=2, engine='python')
coordenadas = coordenadas.drop(columns =0,axis=1).to_numpy()
print("Matriz Coordenadas: ")
print(coordenadas)
cant_variables = coordenadas.shape[0]


poblacion = np.full((h, cant_variables), fill_value=-1, dtype=int)
for i in range(h):
    poblacion[i][0] = np.random.randint(cant_variables)
print("Poblacion inicial :")
print(poblacion)


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





mejor_solucion = np.arange(0,cant_variables)
np.random.shuffle(mejor_solucion)
mejor_costo = Calcular_costo(cant_variables,mejor_solucion,distancias)
print(mejor_costo)

solucionMejorIteracion = 0

Tij0=1/(cant_variables*mejor_costo)
matriz_feromona = np.full_like(distancias,fill_value=Tij0,dtype=float)
print(matriz_feromona)

generacion = 0
while generacion < itereaciones and not (np.round(mejor_costo,decimals=4) == 7544.3659):
    generacion+=1
    print('Generacion: ',generacion)
