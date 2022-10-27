import numpy as np
import pandas as pd
import sys 



if len(sys.argv) == 8:
    seed = int(sys.argv[1])
    h = int(sys.argv[2])
    itereaciones = int(sys.argv[3])
    tasa_evap = int(sys.argv[4])
    importancia_heuristica = float(sys.argv[5])
    probabilidad_exp = int(sys.argv[6])
    archivo = str(sys.argv[7])
    print('Semilla: ', seed)
    print('Tamaño poblacion: ', h)
    print('Numero iteraciones: ', itereaciones)
    print('Tasa de evaporacion: ', tasa_evap)
    print('Peso del valor de heuristica: ', importancia_heuristica)
    print('Probabilidad de exploracion: ', probabilidad_exp)
    print('Matriz: ', archivo)
else:
    sys.exit(0)

np.random.seed(seed)
tasa_evap = tasa_evap/100
probabilidad_exp = probabilidad_exp/100

def Calcular_costo(n,s,c):
    aux = c[s[n-1]][s[0]]
    for i in range(n-1):
        aux += c[s[i]][s[i+1]]
    return aux

def Valor_FeromonaxHeuristica(heuristica, matriz_feromona, memoria,k):
    TxN = memoria[k]*matriz_feromona[poblacion[k][i]]*(heuristica[poblacion[k][i]]**importancia_heuristica)
    return TxN

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
# print("Tij0: ", Tij0)
matriz_feromona = np.full_like(distancias,fill_value=Tij0,dtype=float)
# print("Matris feromona: ",matriz_feromona)





generacion = 0
while generacion < itereaciones and not (np.round(mejor_costo,decimals=4) == 7544.3659):
    generacion+=1
    print('Generacion: ',generacion)
    poblacion = np.full((h, cant_variables), fill_value=-1, dtype=int)
    memoria = np.full_like(poblacion,1,dtype=int)
    trayectoria = np.full_like(poblacion,1,dtype=int)
    for i in range(h):
        aux = np.random.randint(cant_variables)
        poblacion[i][0] = aux
        memoria[i][aux] = 0
    print("Poblacion inicial :")
    print(poblacion)
    print("tray: ", trayectoria)
    print("Memoria: ")
    print(memoria)

    for j in range(cant_variables):
        for k in range(h):
            TxN = Valor_FeromonaxHeuristica(heuristica,matriz_feromona,memoria,k)
            index = np.where(TxN == np.amax(TxN))[0]
            memoria[k][index] = 0
            trayectoria[k][j] = index[0]
