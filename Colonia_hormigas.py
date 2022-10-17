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





poblacion = np.zeros((n,52),int)
for k in range(n):
	poblacion[k]=np.arange(0,52)
	np.random.shuffle(poblacion[k])
print("Poblacion inicial :")
print(poblacion)