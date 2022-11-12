from traceback import print_tb
import numpy as np
import pandas as pd
import sys 
import time


if len(sys.argv) == 8:
    Seed = int(sys.argv[1])
    Tamaño_colonia = int(sys.argv[2])
    Iteraciones = int(sys.argv[3])
    Tasa_evap = int(sys.argv[4])
    Peso_heuristica = float(sys.argv[5])
    Probabilidad_mínima = int(sys.argv[6])
    Archivo_entrada = str(sys.argv[7])
    print('Semilla: ', Seed)
    print('Tamaño poblacion: ', Tamaño_colonia)
    print('Numero iteraciones: ', Iteraciones)
    print('Tasa de evaporacion: ', Tasa_evap)
    print('Peso del valor de heuristica: ', Peso_heuristica)
    print('Probabilidad de exploracion: ', Probabilidad_mínima)
    print('Matriz: ', Archivo_entrada)
    
    if(Seed < 0):
        print("Error: El número de la semilla debe ser positivo\nIngrese un número de semilla positivo")
        sys.exit(0)
    if(Tamaño_colonia <= 1):
        print("Error: El tamaño de la colonia debe ser mayor a 1\nIngrese un tamaño de colonia mayor a 1")
        sys.exit(0)
    if(Iteraciones <= 1):
        print("Error: El número de iteraciones debe ser mayor a 1\nIngrese un número de iteraciones mayor a 1")
        sys.exit(0)
    if(Tasa_evap < 0 or Tasa_evap > 100):
        print("Error: La tasa de evaporación debe ser entre 0 y 100\nIngrese una tasa de evaporación entre 0 y 100")
        sys.exit(0)
    if(Peso_heuristica < 2 or Peso_heuristica > 5):
        print("Error: El factor heurístico debe ser entre 2 y 5\nIngrese un factor heurístico entre 2 y 5")
        sys.exit(0)
    if(Probabilidad_mínima < 0 or Probabilidad_mínima > 100):
        print("Error: La probabilidad mínima debe ser entre 0 y 100\nIngrese una probabilidad mínima entre 0 y 100")
        sys.exit(0)
else:
    print("Error: Los datos ingresados no son validos, ingrese los datos de la siguiente manera:")
    print("python.exe .\Reinas.py Seed Tamaño_colonia Número_Iteraciones Tasa_evaporación Peso_heuristica Probabilidad_mínima Archivo_entrada")
    sys.exit(0)

np.random.seed(Seed)
Tasa_evap = Tasa_evap/100
Probabilidad_mínima = Probabilidad_mínima/100
tiempo_proceso_ini = time.time()

def Calcular_costo(n,s,c):
    aux = c[s[n-1]][s[0]]
    for i in range(n-1):
        aux += c[s[i]][s[i+1]]
    return aux

def Valor_FeromonaxHeuristica(heuristica, matriz_feromona, memoria,k):
    TxN = memoria[k]*matriz_feromona[poblacion[k][i]]*(heuristica[poblacion[k][i]]**Peso_heuristica)
    return TxN


coordenadas = pd.read_table(Archivo_entrada, header = None,delim_whitespace=True, skiprows=6, skipfooter=2, engine='python')
coordenadas = coordenadas.drop(columns =0,axis=1).to_numpy()
# print("Matriz Coordenadas: ")
# print(coordenadas)
cant_variables = coordenadas.shape[0]



distancias = np.full((cant_variables,cant_variables), fill_value=-1.0,dtype=float)
for i in range(cant_variables-1):
    for j in range(i+1,cant_variables):
        distancias[i][j] = np.sqrt(np.sum(np.square(coordenadas[i]-coordenadas[j])))
        distancias[j][i] = distancias[i][j]
# print("Matriz Distancias: ")
# print(distancias)

heuristica = np.full_like(distancias,fill_value=1/distancias, dtype=float)
np.fill_diagonal(heuristica,0)
# print("Matriz Heuristica: ")
# print(heuristica)





mejor_solucion = np.arange(0,cant_variables)
np.random.shuffle(mejor_solucion)
mejor_costo = Calcular_costo(cant_variables,mejor_solucion,distancias)
# print(mejor_costo)

solucionMejorIteracion = 0

Tij0=1/(cant_variables*mejor_costo)
# print("Tij0: ", Tij0)
matriz_feromona = np.full_like(distancias,fill_value=Tij0,dtype=float)

# print("Matriz feromona: ",matriz_feromona)
# print("mejor: ", mejor_costo)
generacion = 0
while generacion < Iteraciones and not (np.round(mejor_costo,decimals=4) == 7544.3659):
    generacion+=1
    print('Generacion: ',generacion)
    # Asignar randómicamente las hormigas en los vértices del grafo
    poblacion = np.full((Tamaño_colonia, cant_variables), fill_value=-1, dtype=int)
    memoria = np.full_like(poblacion,1,dtype=int)
    for i in range(Tamaño_colonia):
        aux = np.random.randint(cant_variables)
        poblacion[i][0] = aux
        memoria[i][aux] = 0
    # print("Poblacion inicial :")
    # print(poblacion)
    # print("Memoria: ")
    # print(memoria)


    for i in range(cant_variables-1):
        for k in range(Tamaño_colonia):
            #Seleccionar el próximo segmento en el grafo
            if np.random.rand() <= Probabilidad_mínima:
                TxN = Valor_FeromonaxHeuristica(heuristica,matriz_feromona,memoria,k)
                j0 = np.random.choice(np.where(TxN == TxN.max())[0])
                # print("j0", j0)
                memoria[k][j0] = 0
                poblacion[k][i+1]= j0
                #Actualizar la feromona en cada segmento según la Ecuación. 4
                matriz_feromona[poblacion[k][i]][poblacion[k][i+1]] = ((1-Tasa_evap)*matriz_feromona[poblacion[k][i]][poblacion[k][i+1]])+(Tasa_evap*Tij0)
                matriz_feromona[poblacion[k][i+1]][poblacion[k][i]] = matriz_feromona[poblacion[k][i]][poblacion[k][i+1]]
            else:
            #Ruleta
                TxN = Valor_FeromonaxHeuristica(heuristica,matriz_feromona,memoria,k)
                total = np.sum(TxN)
                pos = np.empty((1, 1), int)
                ruleta = TxN/total
                ruleta = np.array(ruleta)
                ruleta = np.cumsum(ruleta)
                # print("ruleta: ")
                # print(ruleta)
                rand = np.random.rand()
                # print("rand: ", rand)
                if ruleta[0] > rand:
                    pos[0][-1]= 0
                else:
                    pos = np.where(ruleta <= rand)
                # print("pos: ",pos[0])
                memoria[k][pos[0][-1]+1] = 0
                poblacion[k][i+1]= pos[0][-1]+1
                #Actualizar la feromona en cada segmento según la Ecuación. 4
                matriz_feromona[poblacion[k][i]][poblacion[k][i+1]] = ((1-Tasa_evap)*matriz_feromona[poblacion[k][i]][poblacion[k][i+1]])+(Tasa_evap*Tij0)
                matriz_feromona[poblacion[k][i+1]][poblacion[k][i]] = matriz_feromona[poblacion[k][i]][poblacion[k][i+1]]
            matriz_feromona[poblacion[k][-1]][poblacion[k][0]] = ((1-Tasa_evap)*matriz_feromona[poblacion[k][i]][poblacion[k][i]])+(Tasa_evap*Tij0)
            matriz_feromona[poblacion[k][0]][poblacion[k][-1]] = matriz_feromona[poblacion[k][-1]][poblacion[k][0]]
        # print("Memoria: ")
        # print(memoria)
    
    #Actualizar la mejor solución del proceso hasta la iteración actual
    for i in range(Tamaño_colonia):
        aux = Calcular_costo(cant_variables,poblacion[i][:],distancias)
        # print("aux: ", aux)
        if aux < mejor_costo:
            mejor_costo = aux
            mejor_solucion = poblacion[i][:]
            
    #Actualizar feromona en segmentos de la mejor solución según la Ecuación. 3
    for i in range(cant_variables):
        for j in range(cant_variables):
            posicion_mejor = np.where(mejor_solucion == i)
            posicion_mejor = int(posicion_mejor[0])
            if(posicion_mejor < cant_variables-1): 
                if((mejor_solucion[posicion_mejor+1]) == j):
                    matriz_feromona[i][j] = ((1-Tasa_evap)*matriz_feromona[i][j]) + (Tasa_evap*(1/mejor_costo))
                else:
                    matriz_feromona[i][j] = ((1-Tasa_evap)*matriz_feromona[i][j]) + 0   

    

    
# print("Poblacion: ")
# print(poblacion)
# print("Memoria: ")
# print(memoria)
print("Mejor solucion:")
print(mejor_solucion)
print("Mejor costo: ", (np.round(mejor_costo,decimals=4)))
tiempo_proceso_fin = time.time()
print("Tiempo de busqueda: ", round(tiempo_proceso_fin-tiempo_proceso_ini, 3), "segundos")