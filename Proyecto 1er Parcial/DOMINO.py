import numpy as np
import random
import tkinter as tk
import math,random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io,color,morphology,measure
from sklearn import datasets
#-------------Graficos3D-------------------
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
#-----------------------------------------
plt.close('all')
tiro=[]
def comeMK():
    fich1 = random.randint(0, 6)
    fich2 = random.randint(0, 6)
    if(len(TiroMK)>0):
        for j in range(len(ManoMK)):
            if(ManoMK[j][0]==fich1 and ManoMK[j][1]==fich2 ):
                fich1 = random.randint(0, 6)
                fich2 = random.randint(0, 6)
                break
            elif(ManoMK[j][1]==fich1 and ManoMK[j][0]==fich2 ):
                fich1 = random.randint(0, 6)
                fich2 = random.randint(0, 6)
                break
            elif(TiroMK[j][1]==fich1 and TiroMK[j][0]==fich2 ):
                fich1 = random.randint(0, 6)
                fich2 = random.randint(0, 6)
                break
            elif(TiroMK[j][1]==fich1 and TiroMK[j][0]==fich2 ):
                fich1 = random.randint(0, 6)
                fich2 = random.randint(0, 6)
                break
    elif(len(TiroMK)==0):
        for j in range(len(ManoMK)):
            if(ManoMK[j][0]==fich1 and ManoMK[j][1]==fich2 ):
                fich1 = random.randint(0, 6)
                fich2 = random.randint(0, 6)
                break
            elif(ManoMK[j][1]==fich1 and ManoMK[j][0]==fich2 ):
                fich1 = random.randint(0, 6)
                fich2 = random.randint(0, 6)
    dn=[fich1,fich2]
    ManoMK.append(dn)
    print(ManoMK)
    return
def GAME(f):
    if(len(TiroMK)>0):
        I=TiroMK[0][0]
        D=TiroMK[-1][1]
        #print([I,D],'I-D')
        #print(f,'F')
        if (f[0]==I and f[1]!=D):
            TiroMK.insert(0,[f[1],f[0]])
        elif (f[1]==I and f[0]!=D):    
            TiroMK.insert(0,[f[0],f[1]])
        elif (f[0]==D and f[1]!=I):    
            TiroMK.append([f[0],f[1]])
        elif (f[1]==D and f[0]!=I):    
            TiroMK.append([f[1],f[0]])
        elif (f[1]==D and f[0]==I):    
            TiroMK.append([f[1],f[0]])
        elif (f[0]==D and f[0]==I):    
            TiroMK.append([f[0],f[1]])
        elif (f[1]==D and f[1]==I):    
            TiroMK.append([f[1],f[0]])
    else:
        TiroMK.append(f)
    print(tirada)
    print(TiroMK)
    return
def acomodado(x,y):
    lista=[]
    a=[]
    for i in range(len(x)):
        a.append(x[i])
        a.append(y[i])
        lista.append(a)
        a.clear()
    return lista
def get_values():
    value1 = entry1.get()
    value2 = entry2.get()
    tiro.append(int(value1))
    tiro.append(int(value2))
    raiz.destroy()
    return
def getV():
    print('Es tu turno...')
    x=int(input('PRIMER VALOR\t'))
    y=int(input('SEGUNDO VALOR\t'))
    f=[x,y]
    return f
def SinMula(mano):
    sal=[]
    m=False
    for i in range(len(mano)):
        for j in range(5,-1,-1):
            if(mano[i][0]==j and mano[i][1]==j ):
                sal.append(i)
                sal.append(j)
                m=True
                break  
    if(m==False):
        sal=[10,10]
    return sal

def TUserMULA(iz,der):
    tir=getV()
    tiroU1=tir[0]
    tiroU2=tir[1]
    X=checador(ManoMK, TiroMK, [tiroU1,tiroU2])

    if(tiroU1>iz and tiroU2>der and X==True):
        T=[tiroU1,tiroU2]
        GAME([tiroU1,tiroU2])
        a=True
        Tuser=False
    elif(X==False):
        a=False
    else:
        print('Te regreso tu ficha, Yo tengo una mula mayor\n')
        T=[iz,der]
        GAME(T)
        Turnos.append(1)
        Tuser=True
        a=True
    return a
def TUser():
    # marco_boton = tk.Frame(raiz)
    # marco_boton.pack(side="bottom")
    t=getV()
    T=[t[0],t[1]]
    c=checador(ManoMK, TiroMK, T)
    if c==False:
        c=False
    else:
        GAME(T)
        c=True
    return c
def TUserF():
    tu=getV()
    tuF=checador(ManoMK,TiroMK,tu)
    if (tuF==False):
        c=False
    else:
        
        T=[tu[0],tu[1]]
        GAME(T)
        c=True
    return c
def SkyNet(hand,t,a):
    I=a[0]
    D=a[1]
    inI=[]
    inD=[]
    inM=[]
    nohand=[]
    nohandI=[]
    nohandD=[]
    iz=0
    d=0
    mu=0
    c=True
    mula=False
    Mm=True
    IZ=False
    DER=False
    if(I==D):
        M=I
        MC=M
        for i in range(len(hand)):
            a=hand[i][0]
            b=hand[i][1]
            if M==a or M==b:
                mu=mu+1
                inM.append(i)
    else:
        for i in range(len(hand)):
            a=hand[i][0]
            b=hand[i][1]
            if I==a or I==b:
                iz=iz+1
                inI.append(i)
            elif D==a or D==b:
                d=d+1
                inD.append(i)
    #-----------escoger valor-----------
    #print(iz,'iz')
    #print(d,'d')
    if((iz>0 or d>0) and mu==0):
        c=True
        if(iz>d):
            MC=I
            #print(iz,'Usamos este valor')
            for k in inI:
                man=hand[k]
                if(man[0]==I):
                    nohand.append(man[1])
                else:
                    nohand.append(man[0])
            Mm=True
            IZ=True
        elif(d>iz):
            MC=D
            #print(d,'Usamos este valor')
            for k in inD:
                man=hand[k]
                #print(man,'Mano')
                if(man[0]==D):
                    nohand.append(man[1])
                else:
                    nohand.append(man[0])
            #print(nohand,'Nohand')
            Mm=True
            DER=True
        elif(d==iz):
            MC=D
            #print(d,'Hay la misma cantidad')
            for k in inI:
                man=hand[k]
                if(man[0]==I):
                    nohandI.append(man[1])
                else:
                    nohandI.append(man[0])
            for k in inD:
                man=hand[k]
                if(man[0]==D):
                    nohandD.append(man[1])
                else:
                    nohandD.append(man[0])
            Mm=False
            DER=True
            IZ=True
    elif(mu>0):
        c=True
        for k in inM:
            man=hand[k]
            if(man[0]==M):
                nohand.append(man[1])
            else:
                nohand.append(man[0])
        Mm=True
        mula=True
    elif(mu==0 and iz==0 and d==0):
        c=False
    #-----------------Contador-----------------
    if(c==True):
        CcI=[]
        CcD=[]
        Cc=[]
        if(Mm==True):
            for j in nohand:
                conteo=0
                for i in hand:
                    if(j==i[0] or j==i[1]):
                        conteo=conteo+1
                #print(conteo,'conteo')
                Cc.append(conteo)
            #print(Cc,'Cc')
            Mc=Cc.index(max(Cc))
            #maxonomax(Cc,nohand)
        elif(Mm==False):
            for j in nohandI:
                conteo=0
                for i in hand:
                    if(j==i[0] or j==i[1]):
                        conteo=conteo+1
                CcI.append(conteo)
            #print(CcI,'CcI')
            McI=CcI.index(max(CcI))
            for j in nohandD:
                conteo=0
                for i in hand:
                    if(j==i[0] or j==i[1]):
                        conteo=conteo+1
                CcD.append(conteo)
            #print(CcD,'CcD')
            McD=CcD.index(max(CcD))
    #------------------------------------------------------
        #print(nohand[Mc],'NohandMc')
        
        #print(MC,'MC')
        if IZ==True and DER==False:
            for i in inI:
                if (hand[i][0]==nohand[Mc] and hand[i][1]==MC) or (hand[i][1]==nohand[Mc] and hand[i][0]==MC):
                    f=hand[i]
                    #print(f,'handi')
                    GAME(f)
                    #print(ManoMK[i],'Comprobar que sea la misma ficha')
                    ManoMK.pop(i)
                    break
        elif mula==True and DER==False and IZ==False:
            for i in inM:
                if (hand[i][0]==nohand[Mc] and hand[i][1]==MC) or (hand[i][1]==nohand[Mc] and hand[i][0]==MC):
                    f=hand[i]
                    #print(f,'handi')
                    GAME(f)
                    #print(ManoMK[i],'Comprobar que sea la misma ficha')
                    ManoMK.pop(i)
                    break
        elif IZ==False and DER==True:
            for i in inD:
                if (hand[i][0]==nohand[Mc] and hand[i][1]==MC) or (hand[i][1]==nohand[Mc] and hand[i][0]==MC):
                    f=hand[i]
                    #print(f,'handi')
                    GAME(f)
                    #print(ManoMK[i],'Comprobar que sea la misma ficha')
                    ManoMK.pop(i)
                    break
        else:
            if(McI>McD):
                for i in inI:
                    if (hand[i][0]==McI and hand[i][1]==MC) or (hand[i][1]==McI and hand[i][0]==MC):
                        f=hand[i]                    
                        #print(f,'handi')
                        GAME(f)
                        #print(ManoMK[i],'Comprobar que sea la misma ficha')
                        ManoMK.pop(i)
                        break
            elif(McD>McI):
                for i in inD:
                    if (hand[i][0]==McD and hand[i][1]==MC) or (hand[i][1]==McD and hand[i][0]==MC):
                        f=hand[i]
                        #print(f,'handi')
                        GAME(f)
                        #print(ManoMK[i],'Comprobar que sea la misma ficha')
                        ManoMK.pop(i)
                        break
            elif(McD==McI):
                for i in inD:
                    if (hand[i][0]==McD and hand[i][1]==MC) or (hand[i][1]==McD and hand[i][0]==MC):
                        f=hand[i]
                        #print(f,'handi')
                        GAME(f)
                        #print(ManoMK[i],'Comprobar que sea la misma ficha')
                        ManoMK.pop(i)
                        break
        #-----------------Acomodo------------------
        # print(f,'f')
        # print(I,'I')
        # print(D,'D')
    
    return c
def comedorU():
    print('Comiste 1 ficha')
    x=input('¿Necesitas comer más?\n')
    if(x=='Yes' or x=='yes' or x=='si' or x=='Si'):
        print('Comiste 2 fichas')
        x1=input('¿Necesitas comer más?\n')
        if(x1=='Yes' or x1=='yes' or x1=='si' or x1=='Si' or x1=='y'):
            print('Comiste 3 fichas')
            x2=input('¿Necesitas comer más?\n')
            if(x2=='Yes' or x2=='yes' or x2=='si' or x2=='Si' or x2=='y'):
                y=False
            else:
                y=True
        else:
            y=True
    else:
        y=True
    return y
def checador(manoM, manoT, mano):
    n1=mano[0]
    n2=mano[1]
    m1="""
    DESCALIFICADO POR TRAMPOS@
    
    ESA FICHA SE ENCUENTRA EN MI MAZO
    """
    m2="""
    DESCALIFICADO POR TRAMPOS@
    
    ESA FICHA YA FUE JUGADA
    """
    mano=True
    for i in range(len(ManoMK)):
        if(manoM[i][0]==n1 and manoM[i][1]==n2 ):
            print(m1)
            mano=False
            break
        elif(manoM[i][1]==n1 and manoM[i][0]==n2 ):
            print(m1)
            mano=False
            break
    for i in range(len(TiroMK)):
        if(manoT[i][0]==n1 and manoT[i][1]==n2 ):
            print(m2)
            mano=False
            break
        elif(manoT[i][1]==n1 and manoT[i][0]==n2 ):
            print(m2) 
            mano=False
            break
    return mano
#-----------------------------------------
ManoMK=[]
TiroMK=[]
Turnos=[]
Tiros=0
tiro=[]
tirada="""Fichas en Juego"""

#Randomizar fichas para la computadora---------------------------------------
for i in range(7):
    fich1 = random.randint(0, 6)
    fich2 = random.randint(0, 6)
    for j in range(len(ManoMK)):
        if(ManoMK[j][0]==fich1 and ManoMK[j][1]==fich2 ):
            fich1 = random.randint(0, 6)
            fich2 = random.randint(0, 6)
            break
        elif(ManoMK[j][1]==fich1 and ManoMK[j][0]==fich2 ):
            fich1 = random.randint(0, 6)
            fich2 = random.randint(0, 6)
            break
    dn=[fich1,fich2]
    ManoMK.append(dn)
print(ManoMK)
print('\n BIENVENIDO AL JUEGO')

# raiz=tk.Tk()
# raiz.title('DOMINO')
# raiz.resizable(1,1)
# raiz.iconbitmap('upiita.ico')
# raiz.geometry('1600x300')
# raiz.config(bg='lightpink')
# # Crear el lienzo para dibujar las fichas
# lienzo = tk.Canvas(raiz, width=500, height=500)
# lienzo.pack()

Tramposo=False
seises=True
Tuser=False
# marco_boton = tk.Frame(raiz)
# marco_boton.pack(side="bottom")
# tU="""
# """
for i in range(len(ManoMK)):
    if(ManoMK[i][0]==6 and ManoMK[i][1]==6 ):
        ManoMK.pop(i)
        T=[6,6]
        TiroMK.append(T)
        print(tirada)
        print(TiroMK)
        # print(ManoMK,'ManoMakina')
        Turnos.append(1)
        seises=False
        Tuser=True
        break
if(seises==True):
    sy=input('Tienes la mula de 6?\t(Y) / (N)\n')
    if(sy=='Y' or sy=='y' or sy=='si' or sy=='SI'):
        T=[6,6]
        TiroMK.append(T)
        Tiros=Tiros+1
        print(tirada)
        print(TiroMK)
        Turnos.append(1)
        Tuser=False
    else:       
        sM=SinMula(ManoMK)
        if(sM[0]>=0 and sM[0]<10):
            sM1=sM[0]
            iz=ManoMK[sM1][0]
            der=ManoMK[sM1][1]
            tiro2=input('¿Tienes alguna mula?\n')
            if(tiro2=='n' or tiro2=='N' or tiro2=='No' or tiro2=='NO'):
                T=[sM[1],sM[1]]
                TiroMK.append(T)
                #Tiros=Tiros+1
                print(tirada)
                print(TiroMK)
                Tuser=True
            else:
                t4=TUserMULA(iz,der)
                if (t4==False):
                    Tramposo=True
                else:   
                    Turnos.append(1)
                    Tiros=Tiros+1
                    Tuser=False
        else:
            t3="""
            No tengo MULAS
            Tira una MULA o cualquier otra ficha"""
            print(t3)
            t4=TUser()
            if t4==False:
                Tramposo=True
            else:
                Tiros=Tiros+1
                Turnos.append(1)
Add=4     
win=2
final=False
if(seises==False):
    Tuser=True
if Tramposo==True:
    final=True
    win=0
cmm=0
while(final== False):
    #print(TiroMK)
    print('TURNO '+str(len(Turnos)))
    if(len(ManoMK)==0):
        final=True
        win=0
        break
    if(Tiros==7):
        final=True
        win=1
        break
    
    if (Tuser==True):
        Tuser=True
        print('Tu turno')
        op=input('\nTiras o Comes\n\n-Tiro\n-Como\n')
        if(op=='Tiro' or op=='tiro'):
            t4=TUserF()
            if t4==False:
                Tramposo=True
                win=0 
                Tuser=False
                
                break
                
            else:
                Tiros=Tiros+1
                Turnos.append(1)
                Tuser=False
        elif(op=='Como' or op=='como'):
            Tiros=Tiros-1
            eat=comedorU()
            if eat==False:
                final=True
                win=0
                break
            else:
                final=False
        Tuser=False
            
    elif(Tuser==False):
        print('Mi turno')
        ACT=[TiroMK[0][0],TiroMK[-1][1]]    
        #print(ACT,'ACTUAL')
        tiro2=SkyNet(ManoMK,TiroMK,ACT)
        if(tiro2==True):
            Turnos.append(1)
            Tuser=True
            #print(ManoMK,'ManoMakina')
        elif(tiro2==False):
            t4="""
            No tengo TIRO
            Procedo a comer"""
            print(t4)
            #tiro3=comeMK()
            cmm=cmm+1
            if(cmm==3):
                final==True
                win=1
                Tuser=True
                break
            Tuser=False
    
if(Tramposo ==True or win==0):
    print('\nGAME OVER\n Perdiste, mejor suerte la próxima')
elif(win==1):
    print('\nGAME OVER\n Felicidades ganaste!!!1')
#raiz.mainloop()