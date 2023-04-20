# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:07:22 2023

@author: ASUS
"""
#Funciones a usar
#------------------------------------------------
def corte(graf1,graf2):
    cortarC = []
    cortarF = []
    umbral = 0;
    for i in range(len(graf1)-1):
        if (graf1[i] == 0 and graf1[i+1] != 0 and graf1[i+1] > umbral) or (graf1[i + 1] == 0 and graf1[i] != 0 and graf1[i] > umbral):
            cortarC.append(i)
    for i in range(len(graf2)-1):
        if (graf2[i] == 0 and graf2[i+1] != 0) or (graf2[i + 1] == 0 and graf2[i] != 0):
            cortarF.append(i)
    return cortarC,cortarF

def Obj(corteC,corteF,ima):
    objetos = []
    umbral = 20
    for c in range(0,len(corteC),2):
        for f in range(0,len(corteF),2):
            if (corteF[f+1] - corteF[f] > umbral) and (corteC[c+1] - corteC[c] > umbral):
                objetos.append(ima[corteF[f]:corteF[f+1],corteC[c]:corteC[c+1]]) 
    return objetos

def divficha(ima):
    if ima.shape[0] > ima.shape[1]:
        corte = round(ima.shape[0]/2)
        ficha = [ima[:corte,:],ima[corte:,:]]
    else:
        corte = round(ima.shape[1]/2)
        ficha = [ima[:,:corte],ima[:,corte:]]
    return ficha

def filtro(ficha):
    filt1_1 = morphology.binary_dilation(ficha[0])
    filt1_2 = morphology.binary_dilation(ficha[1])
    filt1_1 = morphology.binary_erosion(filt1_1)
    filt1_2 = morphology.binary_erosion(filt1_2)
    io.imsave("filt1.jpg",filt1_1)
    io.imsave("filt2.jpg",filt1_2)
    return filt1_1,filt1_2

def circulos():
    img1 = cv.imread("filt1.jpg")
    img2 = cv.imread("filt2.jpg")
    img1 = cv.medianBlur(img1, 3)
    img2 = cv.medianBlur(img2, 3)
    img1 = cv.GaussianBlur(img1, (5, 5), 0)
    img2 = cv.GaussianBlur(img2, (5, 5), 0)
    gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    circles1 = cv.HoughCircles(gray_img1, cv.HOUGH_GRADIENT, 0.000001, 10,param1=70, param2=30, minRadius=0, maxRadius=0)
    circles2 = cv.HoughCircles(gray_img2, cv.HOUGH_GRADIENT, 0.000001, 10,param1=70, param2=30, minRadius=0, maxRadius=0)
    if circles1 is None:
        circles1 = circles1
    else:
        circles1 = np.uint16(np.around(circles1))
    if circles2 is None:
        circles2 = circles2
    else:
        circles2 = np.uint16(np.around(circles2))
    return circles1,circles2,gray_img1,gray_img2

def Ratificar(circulos):
    if circulos is None:
        return circulos
    else:
        circs = circulos[0,:]
        for i in range(circs.shape[0]):
            if circs[i][2] >= 80 and circs[i][2]:
                np.delete(circs, i)
    return circs
    
def contar(c1,c2,fichas):
    if (c2 is None and c1 is None):
        fichas.append([0,0])
    elif c2 is None and len(c1) != 0:
        fichas.append([c1.shape[0],0])
    elif c1 is None and  len(c2) != 0:
        fichas.append([0,c2.shape[0]])
    else:
        fichas.append([c1.shape[0],c2.shape[0]])
    return fichas
#------------------------------------------------

#Procesamiento de toda nuestra imagen
#------------------------------------------------
import cv2 as cv
from skimage import io,color,morphology
import matplotlib.pyplot as plt
import numpy as np
#------------------------------------------------
plt.close("all")
fichas = io.imread("foto.jpg")
# plt.figure()
# plt.imshow(fichas)
fic_gris = color.rgb2gray(fichas)
plt.figure()
plt.imshow(fic_gris,cmap='gray')
#------------------------------------------------

fic_binario = (fic_gris > 0.34).astype(np.int16)
plt.figure()
plt.imshow(fic_binario,cmap='gray')

# fs = filters.sobel(fic_binario)
# plt.figure()
# plt.imshow(fs,cmap='gray')

sumC = np.sum(fic_binario,axis=0)
plt.figure()
plt.plot(sumC)

sumF = np.sum(fic_binario,axis=1)
plt.figure(7)
plt.plot(sumF)


corteC,corteF = corte(sumC,sumF)
ficha_sep = Obj(corteC,corteF,fic_binario)
fichas= [] 
for i in ficha_sep:
    fic = divficha(i)
    [filt1,filt2] = filtro(fic)
    [c1,c2,img1,img2] = circulos()
    c1 = Ratificar(c1)
    c2 = Ratificar(c2)
    # for i in c1:
    #     cv.circle(img1,(i[0],i[1]), i[2], (50,50,50),4)
    # for i in c2:
    #     cv.circle(img2,(i[0],i[1]), i[2], (50,50,50),4)
    fichas = contar(c1,c2,fichas)
#-----------------------------------------------

