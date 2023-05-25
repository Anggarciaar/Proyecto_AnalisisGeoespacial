import geopandas as gpd
pozos= gpd.read_file('C:\\Users\\loren\\OneDrive\\Documents\\data\\Banco_de_Informaci_C3_B3n_Petrolera_3A_Pozos\\Banco_de_Informaci_C3_B3n_Petrolera_3A_Pozos.shp')
print(pozos)
import numpy as np
import pandas as pd
import pysal
import seaborn as sbn
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.neighbors import KernelDensity
X = pozos.geometry.apply(lambda geom: (geom.x, geom.y)).tolist()
kde = KernelDensity()
kde.fit(X)
print(kde)