import numpy as np
import pandas as pd
import sys 


df = pd.read_table('berlin52.tsp', header = None,delim_whitespace=True, skiprows=6, skipfooter=2, engine='python')
df = df.drop(columns=0,axis=1).to_numpy()
print(df)
variables = df.shape[0]
print(variables)

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

