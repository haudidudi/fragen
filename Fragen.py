# -*- coding: utf-8 -*-

import pandas as pd    
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#1. Versuch: gibt mir die richtigen y Werte aber mit falscher xAchse(normale Indizierung nicht die Spalte aus der Datei)
raman_spectrum = pd.read_csv("Si0.txt", sep="\t", header=0, names=["xAchse", "yAchse"])
print(raman_spectrum.head())

rs = pd.Series(raman_spectrum["yAchse"])
rs.plot()
plt.show()


#2. Versuch: Versuch den index auf die erste Spalte zu setzen - fail - beide Achsen nur noch im Bereich -0,06 bis +0,06 - why?
raman_spectrum = pd.read_csv("Si0.txt", sep="\t", header=0, names=["xAchse", "yAchse"])
print(raman_spectrum.head())

rs = pd.Series(raman_spectrum["yAchse"], index=raman_spectrum["xAchse"])
rs.plot()
plt.show()


#3.Versuch: genau das gleiche 
raman_spectrum = pd.read_csv("Si0.txt", sep="\t", header=0, names=["xAchse", "yAchse"])
print(raman_spectrum.head())

rs = pd.Series(raman_spectrum["yAchse"], raman_spectrum["xAchse"])
rs.plot()
plt.show()