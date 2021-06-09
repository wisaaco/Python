#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:16:40 2021

@author: isaaclera
"""

import numpy as np

data = np.array([1,0]) 

#Actividad1
l = np.arange(10)
np.repeat([l],10,axis=0)


#Actividad2
v1 = np.arange(1,4)
v2 = np.arange(4,7)
np.sqrt(np.sum(np.square(v1-v2)))
np.linalg.norm(v1-v2)


#Actividad2
v1 = np.arange(1,4)
v2 = np.arange(4,7)
np.sum(np.absolute(v1-v2))
np.sum(np.abs(v1-v2))


#Actividad3
l = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
l[np.where(l%2)]=-1
np.where(l%2==1,-1,l)
np.where(a%2!=0, -1*np.ones(10, dtype=np.int8), a)

#Actividad4
l = np.array([0, 1, 1, 1, 4, 5, 6, 7, 7, 7])
pos = np.unique(l,return_index=True)[1]
sol = np.array([True]*l.shape[0]) # no elegante
sol = np.full(l.shape[0],True) # mas cool
sol[pos]=False

#Actividad5
l = np.array([0, 1, 5, 3, 65, 54, 6, 7, 80, 9])
dif = np.diff(np.sign(np.diff(l)))
np.where(dif==-2)[0]+1

np.where(l[1:]<[l[0:-1]])[1] #alerta, con v.izq

#Actividad 6
case = np.array([[5,3,0,0,7,0,0,0,0],
                 [6,0,0,1,9,5,0,0,0],
                 [1,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 [3,6,0,0,0,0,2,8,0],
                 [3,0,0,4,1,9,0,0,5],
                 [0,0,0,0,8,0,0,7,9]])

np.any(np.sum(case>0,axis=0)==8)
np.any(np.sum(case>0,axis=1)==8)

#Actividad 7 
### RETO pendiente