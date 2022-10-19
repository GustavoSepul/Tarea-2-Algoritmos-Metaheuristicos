from math import e
from pickle import NONE
import numpy as np
import pandas as pd
import sys 


# df = pd.read_csv('berlin52.txt', sep =" ", header = None)
# print(df)

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