# -*- coding: utf-8 -*-
"""
Programa que solo va a probaar la función de las camaras

@author: HP
"""

# Incluir las librerias a utilizar
#----------------------------------------------------
import cv2
from skimage import io
import matplotlib.pyplot as plt
#----------------------------------------------------
# Se lee la camara y se obtiene la foto
cam = cv2.VideoCapture(1
                       )
print("Cuando las fichas de la maquina esten listas para la foto presiona s")
while(True):
    ret, frame = cam.read()
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Guardar la imagen
        io.imsave('foto.jpg', frame)
        break
    cv2.imshow('frame',frame) # Se va a comentar despues de lograr todas las pruebas
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
cam.release()
cv2.destroyAllWindows()
#----------------------------------------------------
#Procesamiento de la imagen
image = io.imread('foto.jpg')
plt.figure()
plt.imshow(image) #Se debe comentar para no mostrar al usuario las fichas de la maquina
