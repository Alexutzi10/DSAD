import numpy as np
import pandas as pd
from functii import nan_replace, acp
from grafice import *

np.set_printoptions(precision=5,threshold=10000,suppress=True)

mortalitate = pd.read_csv("mortalitate_ro.csv", index_col=1)
valori_lipsa = mortalitate.isna().any().any()
if valori_lipsa:
    nan_replace(mortalitate)
    print("Valori lipsa inlocuite!")

variabile = list(mortalitate)[1:]
model_acp = acp(mortalitate, variabile)
model_acp.fit()
print("Varianta componente:")
print(model_acp.alpha)
print("Vectorii axe (saturatiile componentelor):")
print(model_acp.a)
print("Componentele principale:")
print(model_acp.c)

print("Criterii:",model_acp.criterii)
k =np.nanmin(model_acp.criterii)
print(k)
plot_varianta(model_acp.alpha,model_acp.criterii)

