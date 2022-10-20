import numpy as np
import pandas as pd
import sys 


df = pd.read_table('berlin52.txt', header = None,delim_whitespace=True, skiprows=6, skipfooter=2)
df = df.drop(columns =0,axis=1).to_numpy()
print(df)
variables = df.shape[0]
print(variables)
# df = pd.read_csv('berlin52.txt', sep =" ", header = None)
# print(df)
# semilla 
# tamaño colonia
# numero iteraciones
# tasa de evaporacion
# factor de importancia euristica (2,5)
# probabilidad exploracion explotacion (0 - 1)
# archivo de entrada

if len(sys.argv) == 3:
    seed = int(sys.argv[1])
    n = int(sys.argv[2])
    print(seed, n)
else:
    sys.exit(0)


poblacion = np.full((n, 52), -1)
for i in range(n):
    poblacion[i][0] = np.random.randint(52)
print("Poblacion inicial :")
print(poblacion)
