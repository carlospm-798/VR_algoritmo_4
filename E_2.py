#Paredes Márquez Carlos
#Ejercicio 2
#24 28 2021
'''Calcula el histograma de la imagen y grafícalo'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

#ig = cv2.imread('Jessy.png',0)
im = cv2.imread('Jessy.png')
ig = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
[M,N] = ig.shape[0:2] #calcular tamaño de la imagen

hist = cv2.calcHist([ig],[0],None,[3],[0,256]).flatten()/(M*N) 
#Para calcular térciales, solo ponemos un 3 en el 4to parámetro
#/(M*N) para calcular la normalización
#imagen, n. canales, mask, tamaño, rango de valores. función de 
#regresar una imagen de una sola dimensión

'''Calcular exposición de la imagen'''

maxElement = np.argmax(hist) #usamos de 0 a 2 por que las series 
if maxElement == 2 and hist[2] > 0.3: #en programación comienzan
    print('Imagen sobreexpuesta') #desde el cero
elif maxElement == 0 and hist[0] > 0.3:
    print('Imagen subexpuesta')
else:
    print('Buena exposición')

cv2.imshow('image0',ig)
cv2.imshow('image1',im)

fig= plt.figure()
plt.bar(range(len(hist)),hist)
plt.show()