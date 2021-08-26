#Paredes Márquez Carlos
#Ejercicio 1
#24 28 2021
'''Calcula el histograma de la imagen y grafícalo'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

ig = cv2.imread('gorillaz.jpg',0)
[M,N] = ig.shape[0:2] #calcular tamaño de la imagen

hist = cv2.calcHist([ig],[0],None,[256],[0,256]).flatten()/(M*N) #/(M*N) para calcular la normalización
#imagen, n. canales, mask, tamaño, rango de valores. función de 
#regresar una imagen de una sola dimensión

cv2.imshow('image0',ig)

fig= plt.figure()
plt.bar(range(len(hist)),hist)
plt.show()
