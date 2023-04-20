# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Librerias que se van a utilizar
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
# -------------------------------------------------------
plt.close('all') #Cerrar todas las ventanas
imagen = io.imread('P1_01.jpeg') #Leer la imagen en la ubicacion donde se encuentra
plt.figure()
plt.imshow(imagen)
numclas = int(input("¿Cuantas clases tiene tu imagen? \n"))
clas = np.zeros([numclas,3])
color = np.zeros([numclas,3])
for n in range(numclas):
    muestras = int(input("¿Cuantas muestras deseas? \n")) #pregunta el numero de muestras a tomar
    a = np.array(plt.ginput(muestras),dtype=int) #Obtiene la fila, columna donde se realizo el click
    b = imagen[a[:,1],a[:,0]] #Obtenemos el color de cada pixel selecciondado
    clas[n,:] = np.average(b,axis=0)
    color[n,:] = np.average(b,axis=0)
# muestras = int(input("¿Cuantas muestras deseas? \n")) #pregunta el numero de muestras a tomar
# a = np.array(plt.ginput(muestras),dtype=int) #Obtiene la fila, columna donde se realizo el click
# b = imagen[a[:,1],a[:,0]] #Obtenemos el color de cada pixel selecciondado
# cla1 = np.average(b,axis=0) #Saca promedio de cada columna
# cla1 = np.array([220,215,211])
# cla2 = np.array([0,112,188])
# cla3 = np.array([122,177,182])
# #cla4 = [201,23,39]
filas = imagen.shape[0]
columnas = imagen.shape[1]
umbral = np.random.randint(10,70,size=numclas)
salida = np.zeros([filas,columnas,3])
for i in range(filas):
    for j in range(columnas):
        R = imagen[i,j,0]
        G = imagen[i,j,1]
        B = imagen[i,j,2]
        DE1 = np.sqrt((R-clas[0,0])**2+(G - clas[0,1])**2+(B - clas[0,2])**2)
        DE2 = np.sqrt((R-clas[1,0])**2+(G - clas[1,1])**2+(B - clas[1,2])**2)
        DE3 = np.sqrt((R-clas[2,0])**2+(G - clas[2,1])**2+(B - clas[2,2])**2)
        dato1 = np.argmin([DE1,DE2,DE3]) 
        dato2 = np.min([DE1,DE2,DE3])
        for select in range(numclas):
            if dato1 == select and dato2 <= umbral[select]:
                salida[i,j,:] = color[select,:]
        # if dato1 == 0 and dato2 <= umbral1:
        #     salida[i,j,0] = 255
        #     salida[i,j,1] = 255
        #     salida[i,j,2] = 255
        # elif dato1 == 1 and dato2 <= umbral2:
        #     salida[i,j,0] = 255
        #     salida[i,j,1] = 0
        #     salida[i,j,2] = 0
        # elif dato1 == 2 and dato2 <= umbral3:
        #     salida[i,j,0] = 0
        #     salida[i,j,1] = 255
        #     salida[i,j,2] = 0
        # else:
        #     salida[i,j,0] = 0
        #     salida[i,j,1] = 0
        #     salida[i,j,2] = 255
salida = np.uint8(salida)
plt.figure()
plt.imshow(salida)


