from pickle import NONE
import numpy as np
import pandas as pd


df = pd.read_table('berlin52.txt', header = None,delim_whitespace=True, skiprows=6, skipfooter=2)
df = df.drop(columns =0,axis=1).to_numpy()
print(df)
variables = df.shape[0]
print(variables)