#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:38:07 2016

@author: Mauro Ferro
License: GNU GPLv3
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print 'Calcolo rata e piano di ammortamento alla francese. \n'
print 'N.B. usare il punto come separatore dei decimali e non la virgola!!! \n'
importo =float(raw_input('Inserire l\'importo: '))
tempo = int(raw_input('Inserire il numero di rate: '))
tasso = float(raw_input('Inserire il tasso : '))
rata = round((1+1/((1+tasso/1200)**tempo - 1))*(tasso/1200)*importo,3)
E = 0
tot_I = 0
R = importo
plan = np.array
plan = [[0,0,0,R]]
print '*'
print ' *'
print'  * Importo della rata: '+ str(rata)
print ' *'
print '*' 

numero_rate = range(0,tempo)
for count in numero_rate:
    I = round(R *tasso/1200,2)
    C = round(rata - I,2)
    R = round(R - C,2)
    E = round(E + C,2)
    tot_I = tot_I + I
    P = tot_I + E
    plan.append([I,C,tot_I,P,E,R])
index = ['Quota Interessi', 'Quota Capitale', 'Totale Interessi', 'Totale Pagato', 'Debito Estinto', 'Debito Residuo']
df = pd.DataFrame(plan)
df.columns = index
print df
df.drop(df.columns[[0,1]], axis=1, inplace= True)
df.plot()
plt.xlabel('Rata n.')
plt.ylabel('Euro')
plt.ylim([0,importo+float(importo*0.1)])
plt.xlim([0,tempo])
plt.show()
