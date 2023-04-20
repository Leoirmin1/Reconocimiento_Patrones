# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:51:26 2023

@author: ASUS
"""
#------------------------------------LIBRERIAS USADAS-----------------------------------------------------------
import tkinter
import customtkinter as ctk
from PIL import Image
from skimage import io,color,morphology
import numpy as np
import os
import cv2
#--------------------------------------------------------------------------------------------------------------

#-------------------------------------------CONFIGURACION INICIAL----------------------------------------------
# Carpeta principal del proyecto
carpeta_principal = os.path.dirname(__file__)
# Carpeta de imágenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")

#Apariencia que va a tener la interfaz grafica
ctk.set_appearance_mode("dark") #Va aser de tema oscuro
ctk.set_default_color_theme("green") #El color de los botones va a ser de color verde

#-------------------------------CLASE DE FRAME-------------------------------------------------------------------
#Una clase para crear frames para las ventanas de las interfaces
class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs): #Inicializa el framework
        super().__init__(master, **kwargs) #Lo crea como una super clase
        self.configure(fg_color="#010101") # Establecemos el color del framework igual al fondo de las ventanas
#----------------------------------------------------------------------------------------------------------------       
        
#---------------------CLASE DE LA VENTANA DE INICIO---------------------------------------------------------------
#La clase que crea la ventana para iniciar el juego
class Inicio:
    
    def __init__(self):
        self.root = ctk.CTk() #Crea la ventana
        self.root.title("Juego de Domino") #Nombre de la ventana
        self.root.configure(fg_color="#010101") #Color del fondo de la ventana
        self.root.geometry("600x500") #Tamaño que tendra la ventana
        self.root.resizable(False,False) #Se pone en False para que no se pueda modificar el tamaño de la ventana
        self.root.iconbitmap(os.path.join(carpeta_imagenes, "domino.ico")) #Se crea el logo como un icono para la ventana
        #Se crea una variable la que contiene la imagen para el inicio
        logo = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes, "domino.png"))), # Imagen modo claro
            size=(200, 200)) # Tamaño de las imágenes
        #Imagen que contiene el logo del IPN con un tamaño de 50,70
        logo_IPN = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"logo-ipn-blanco.png"))),size=(50,70))
        #Imagen que contiene el logo de UPIITA con un tamaño de 70,90
        logo_Upiita = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"logo-upiita-blanco.png"))),size=(70,90))
        self.root.grid_rowconfigure(0, weight=1) #Se congigura las filas del grid de la ventana
        self.root.grid_columnconfigure(0, weight=1) #Se congigura las columnas del grid de la ventana
        self.my_frame = MyFrame(master=self.root) #Se crea un frame para la ventana
        self.my_frame.grid(row=0, column=0, padx=20, pady=30) #Se configura el grid del framework
        self.my_frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER) #Se establece la ubicacion del framework en la ventana
        
        etiqueta = ctk.CTkLabel(master=self.my_frame,image=logo,text="") #Se crea una etiqueta que contiene la imagen de logo para mostrarla
        etiqueta.grid(row=0,column=2, padx = 100) # Se pone en que posicion del frame va a estar
        
        #Se crea una etiqueta para mostrar la imagen del IPN
        etIPN = ctk.CTkLabel(master=self.my_frame,
                               image=logo_IPN,
                               text="")
        etIPN.grid(row=3,column=0) #Se establece en que posicio del frame se encuentra
        #Se crea una etiqueta para mostrar la imagen de UPIITA
        etUpiita = ctk.CTkLabel(master=self.my_frame,
                               image=logo_Upiita,
                               text="")
        etUpiita.grid(row=3,column=3)#Se establece la posicion de la etiqueta en el frame
        
        #Se crea un boton el cual al dar click iniciara la siguiente ventana
        Inbot = ctk.CTkButton(self.my_frame,text="Comenzar a jugar",command=self.Juego)
        #Establecemos la posicion del boton en el frame
        Inbot.grid(row=1,column=2,padx=100, pady=20)
        #Creamos otro boton el cual este cerrara el programa
        Sabot = ctk.CTkButton(self.my_frame,text="Salir",command=self.Cerrar)
        #Se establece la posicion del boton
        Sabot.grid(row=2,column=2,padx=10, pady=20)
        #Se mantiene en loop la ventana para que se siga mostrando
        self.root.mainloop()
        
    def Cerrar(self):
        #Funcion que cierra el programa
        self.root.destroy()
        
    def Juego(self):
        #Funcion que cierra la ventana de Inicio y ejecuta la siguiente ventana
        #donde se llevara a cabo la toma y el procesado de las fichas de domino
        self.root.destroy()
        Es = Espera()
        
#--------------------------------------------------------------------------------------------------------------

#----------------------CLASE DE LA VENTANA DE PROCESADO--------------------------------------------------------
# Esta clase es la ventana para la toma de las fotos y el procesado para reconocer la ficha de domino
# ingresada mediante la toma de una foto
class Espera:
    def __init__(self):
        self.root = ctk.CTk() #Se crea la nueva ventana
        self.root.title("Juego de Domino") # El nombre de la ventana
        self.root.iconbitmap(os.path.join(carpeta_imagenes, "domino.ico"))# Se le añade un icono a la ventana
        self.root.geometry("640x480") # Se establece su tamaño de la ventana
        self.var = False # Se crea una variable de tipo booleana
        self.Loading() # Se manda a llamar a la funcion Loading
        self.root.update_idletasks() #Actualiza todos los botones
        self.root.update() #Actualiza toda la ventana
        self.root.after(1000) #Espera un segundo
        self.label.configure(text='Presiona el boton para tomar la foto') # Se cambia el texto de la etiqueta
        self.Fichas= [] #Se crea la variable de Fichas para aqui guardar los valores de las fichas
        while self.var == False: #Se quedara en este ciclo hasta que la variable self.var se cambie a True
            self.ret, self.frame = self.cam.read() # Se estara leyendo constantemente los frames de la camara
            cv2.imshow('frame',self.frame) #Muestra en una ventana cv2 lo que se muestra en la camara
            self.root.after(1) #Se espera 1ms para despues volver a actualizar el frame
            self.root.update_idletasks() #Se actualiza los botones para poder usarlos
            self.root.update() #Se actualiza la ventana 
        self.root.mainloop() #Se mantiene el loop de la ventana
        
    def Loading(self): 
        #Funcion que cambiara el texto de la etiqueta de cargando y creara el boton para tomar las fotos 
        self.label = ctk.CTkLabel(master= self.root,text="Cargando ....")
        self.label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) # Establece la posicion de la etiqueta al centro
        #Se crea un boton para tomar la foto y que se procese la imagen
        capt = ctk.CTkButton(master=self.root,text="Tomar Foto",command = self.Capture)
        #se establece la posicion del boton
        capt.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)
        # Se inicializa la camara a usar para tomar las fotos
        self.cam = cv2.VideoCapture(1)
        
    def Capture(self):
        #Funcion en la que toma la imagen y la procesa siempre y cuando no se tengan 7 fichas
        # cuando se tienen las 7 fichas se destruye la ventana y se inicia la ventana del juego de domino
        if len(self.Fichas) == 7: #Si se tiene en la variable fichas una longitud de 7 realiza lo siguiente
            self.var == True #Se cambia a true para quitar el ciclo while que se usa para ir leyendo los frames del video
            self.cam.release() #Se libera la camara y los recursos que se usaron
            cv2.destroyAllWindows() #Se destrulle todas las ventanas que se hayan abierto de la libreria OpenCV
            self.root.destroy() #Se destruye la ventana
            Jg = Juegos(self.Fichas) # Se inicia la siguiente ventana con la variable Fichas, ya que la necesita para empezar el juego
        else: # si no tiene esa longitud la variable hace esto
            io.imsave('foto.jpg', self.frame) #Guarda la foto tomafa como 'foto.jpg' 
            self.image = io.imread('foto.jpg') #Lee la foto que se guardo en la instruccion anterior
            num_fichas = len(self.Fichas) + 1 # se usa para ver cuantas fichas se han registrado
            texto = 'Se han procesado '+ str(num_fichas) + ' fichas' # Texto para ponerlo despues en el label de la interfaz
            self.label.configure(text=texto) # Se cambia el texto de la etiqueta
            self.root.update() # Se actualiza la ventana para que se refleje los cambios
            self.root.after(500) #Se espera 500 ms para poder leer
            self.Procesing() #Se llama a la funcion Procesing
            self.label.configure(text=self.Fichas) # Se cambia el texto para saber que ficha reconocio, se puede comentar si no se quiere saber las fichas de la maquina
            self.root.update() # Se actualiza la ventana para que se refleje los cambios
            self.root.after(500) #Se espera 500 ms para poder leer
        
        
    def Procesing(self):
        #Funcion que realiza todo el procesado de la imagen que se tomo
        fic_gris = color.rgb2gray(self.image) #Se convierte la imagen a escala de grises
        fic_binario = (fic_gris > 0.34).astype(np.int16) #Después se binariza la imagen a escala de grises
        sumC = np.sum(fic_binario,axis=0) #Se suma los unos en las columnas 
        sumF = np.sum(fic_binario,axis=1) #Se suma los unos en  las filas
        corteC,corteF = self.corte(sumC,sumF) #Se manda a llamar a la funcion corte que ocupa sumC y sumf
        ficha_sep = self.Obj(corteC,corteF,fic_binario) #Se manda a llamar la funcion Obj que ocupa corteC,corteF y la imagen binarizada
        for i in ficha_sep: #Se itera los elementos que hay en la variable ficha_sep
            fic = self.divficha(i) #Se manda a llamar la funcion de divficha para cada valor en la lista ficha_Sep
            self.filtro(fic) #Se llama la funcion filtro para la variable fic
            [c1,c2,img1,img2] = self.circulos() #Se manda a llamar la funcion circulos
            c1 = self.Ratificar(c1) #Se manda a llamar la funcion Ratificar para la variable c1
            c2 = self.Ratificar(c2) #Se manda a llamar la variable Ratificar para c2
            self.Fichas = self.contar(c1,c2,self.Fichas) #Se manda a llamar la funcion contar
    
    def corte(self,graf1,graf2):
        #Funcion la cual encontrara donde se debe cortar la imagen para obtener cada ficha de la imagen o la ficha dependiendo de 
        #cuantas fichas se hayan colocado en la foto
        cortarC = [] # Se crea una variable de tipo lista
        cortarF = [] # Se crea una variable de tipo lista
        for i in range(len(graf1)-1): # Ciclo for para iterar la variable graf1
            #Se añadira el valor de i cuando el valor en la graf1 pasa de 0 a un valor alto o de un valor a 0
            if (graf1[i] == 0 and graf1[i+1] != 0) or (graf1[i + 1] == 0 and graf1[i] != 0): 
                #Se añade el valor de i a la variable cortarC
                cortarC.append(i)
        for i in range(len(graf2)-1): #Ciclo for para iterar la variable graf2
            #Se añadira el valor de i cuando el valor en la graf1 pasa de 0 a un valor alto o de un valor a 0
            if (graf2[i] == 0 and graf2[i+1] != 0) or (graf2[i + 1] == 0 and graf2[i] != 0):
                #Se añade el valor de i a cortarF
                cortarF.append(i)
        return cortarC,cortarF #Se regresa el valor de las variables corteC y corteF

    def Obj(self,corteC,corteF,ima):
        #Funcion la cual cortara la imagen para obtener la ficha de la imagen
        objetos = [] # Variable en la que se guardara cada ficha 
        umbral = 50 # Variable para descaartar cosas que no sean una ficha
        for c in range(0,len(corteC),2): #Iteracion con un paso de 2 en corteC
            for f in range(0,len(corteF),2): #Iteracion con un paso de 2 en corteF
            #Si el valor siguiente y el actual superan el umbral para las dos variables se corta la imagen
                if (corteF[f+1] - corteF[f] > umbral) and (corteC[c+1] - corteC[c] > umbral):
                    #Se guarda el corte de la imagen binarizada en la varible objetos
                    objetos.append(ima[corteF[f]:corteF[f+1],corteC[c]:corteC[c+1]]) 
        return objetos #Se regresa la variable objetos
 
    def divficha(self,ima): 
        #Funcion la cual dividira las fichas a la mitad para poder determinar
        if ima.shape[0] > ima.shape[1]: #Si es mas grande las filas que las columnas
            #Corte es el valor medio de la imagen redondeada
            corte = round(ima.shape[0]/2)
            #Se procede a crear los cortes en la mitad de la ficha
            ficha = [ima[:corte,:],ima[corte:,:]]
        else: #Si es mas grande las columnas el corte se hara en las columnas
            #Se obtiene el valor medio de las columnas
            corte = round(ima.shape[1]/2)
            #Se corta la imagen por la mitad pero por las columnas
            ficha = [ima[:,:corte],ima[:,corte:]]
        return ficha #Se regresa la variable ficha
    
    def filtro(self,ficha):
        #Se va a realizar aqui un filtro de dilatacion y erosion binaria para separar mejor las figuras
        filt1_1 = morphology.binary_dilation(ficha[0])
        filt1_2 = morphology.binary_dilation(ficha[1])
        filt1_1 = morphology.binary_erosion(filt1_1)
        filt1_2 = morphology.binary_erosion(filt1_2)
        # Se guardan ambas imagenes
        io.imsave("filt1.jpg",filt1_1)
        io.imsave("filt2.jpg",filt1_2)
    
    def circulos(self):
        #Esta funcion utiliza la transformada de Hough para encontrar el radio y el centro de los circulos en la imagen
        #Se leen las imagenes pero con la libreria cv2, para poder usar la funcion de HoughCircles de OpenCV
        img1 = cv2.imread("filt1.jpg")
        img2 = cv2.imread("filt2.jpg")
        #Se realiza un filtro medianblur el cual elimina el ruido en la imagen y mejora la calidad de esta
        img1 = cv2.medianBlur(img1, 3)
        img2 = cv2.medianBlur(img2, 3)
        #Se usa un filtro gausiano para suavizar la imagen para mejorar el resultado de la transformada de Hough
        img1 = cv2.GaussianBlur(img1, (5, 5), 0)
        img2 = cv2.GaussianBlur(img2, (5, 5), 0)
        #Se transforma a escala de grises por que no se detecta bien la binarizacion
        gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        #Se realiza la transformada de Hough para determinar la cantidad de circulos que se detectan
        circles1 = cv2.HoughCircles(gray_img1, cv2.HOUGH_GRADIENT, 0.000001, 10,param1=70, param2=30, minRadius=0, maxRadius=0)
        circles2 = cv2.HoughCircles(gray_img2, cv2.HOUGH_GRADIENT, 0.000001, 10,param1=70, param2=30, minRadius=0, maxRadius=0)
        #Si no se detectan los circulos o no hay regresa una variable vacia 
        if circles1 is None: # Si la variable es vacia
            circles1 = circles1 #Se queda el valor igual
        else: #Si no
            circles1 = np.uint16(np.around(circles1)) #Se redondean los valores de circles y se ponen en uint16
        #Si se regresa la variable vacia la deja igual
        if circles2 is None:
            circles2 = circles2 #Se queda igual la variable
        else: #Si no
            circles2 = np.uint16(np.around(circles2)) #Se redondean sus valores y se ponen en uint16
        return circles1,circles2,gray_img1,gray_img2 #Se regresan las imagenes y los circulos

    def Ratificar(self,circulos): 
        #Esta función ratifica los circulos
        if circulos is None: #Si la variable esta vacia
            return circulos #Regresa la variable 
        else: #Si no
            circs = circulos[0,:] #Se agarra lo que hay dentro de la lista de listas
            for i in range(circs.shape[0]): #Se itera por el numero de circulos que hay
                if circs[i][2] >= 80: #Si el radio del circulo es mayor a 80   
                    np.delete(circs, i) #Lo elimina de la lista
        return circs #Regresa circs
        
    def contar(self,c1,c2,fichas):
        #Funcion en la que cuenta la cantidad de circulos que hay
        if (c2 is None and c1 is None): #Si ambas listas estan vacias 
            fichas.append([0,0]) #Se le añade a fichas la mula del 0
        elif c2 is None and len(c1) != 0: #Si la lista de c2  esta vacia y la otra no
            fichas.append([c1.shape[0],0]) #Se añade la ficha [c1,0] 
        elif c1 is None and  len(c2) != 0: #Si la lista c1 esta vacia y la otra no
            fichas.append([0,c2.shape[0]]) #Se añade la ficha [0,c2]
        else: #Si ambas listas tienen numero
            fichas.append([c1.shape[0],c2.shape[0]]) #Se añade la ficha [c1,c2]
        return fichas #Se regresa la variable fichas
    
class Juegos:
    
    def __init__(self,Fichas):
        self.root = ctk.CTk()
        self.root.title("Juego de Domino")
        self.root.configure(fg_color="#010101")
        self.root.geometry("1080x640,1000,250")
        self.root.resizable(False,False)
        self.root.iconbitmap(os.path.join(carpeta_imagenes, "domino.ico"))
        self.juego = MyFrame(master=self.root,width=1000)
        self.juego.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.Tramposo=False
        self.seises=True
        self.Tuser=False
        self.ManoMK= Fichas
        self.TiroMK=[]
        self.Turnos=[]
        self.Tiros=0
        self.tiro=[]
        self.tirada="""Fichas en Juego"""
        self.var = ctk.BooleanVar()
        self.var1 = ctk.BooleanVar()
        self.var2 = ctk.BooleanVar()
        self.var3 = ctk.BooleanVar()
        self.varFicha = ctk.BooleanVar()
        #=======>Cargamos todas las imagenes que se usan para los botones<=========
        
        F0_0 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F0-0.jpg"))),size=(60,30))
        F0_1 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F0-1.jpg"))),size=(60,30))
        F0_2 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F0-2.jpg"))),size=(60,30))
        F0_3 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F0-3.jpg"))),size=(60,30))
        F0_4 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F0-4.jpg"))),size=(60,30))
        F0_5 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F0-5.jpg"))),size=(60,30))
        F0_6 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F0-6.jpg"))),size=(60,30))
        F1_1 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F1-1.jpg"))),size=(60,30))
        F1_2 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F1-2.jpg"))),size=(60,30))
        F1_3 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F1-3.jpg"))),size=(60,30))
        F1_4 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F1-4.jpg"))),size=(60,30))
        F1_5 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F1-5.jpg"))),size=(60,30))
        F1_6 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F1-6.jpg"))),size=(60,30))
        F2_2 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F2-2.jpg"))),size=(60,30))
        F2_3 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F2-3.jpg"))),size=(60,30))
        F2_4 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F2-4.jpg"))),size=(60,30))
        F2_5 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F2-5.jpg"))),size=(60,30))
        F2_6 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F2-6.jpg"))),size=(60,30))
        F3_3 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F3-3.jpg"))),size=(60,30))
        F3_4 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F3-4.jpg"))),size=(60,30))
        F3_5 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F3-5.jpg"))),size=(60,30))
        F3_6 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F3-6.jpg"))),size=(60,30))
        F4_4 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F4-4.jpg"))),size=(60,30))
        F4_5 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F4-5.jpg"))),size=(60,30))
        F4_6 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F4-6.jpg"))),size=(60,30))
        F5_5 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F5-5.jpg"))),size=(60,30))
        F5_6 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F5-6.jpg"))),size=(60,30))
        F6_6 = ctk.CTkImage(dark_image=Image.open((os.path.join(carpeta_imagenes,"F6-6.jpg"))),size=(60,30))
        
        
        #===========================================================================
        regbot = ctk.CTkButton(master=self.root,text = "Regresar",width= 100,height=32,command = self.Regresar)
        regbot.place(relx=0.05,rely=0.05)
        
        self.compu = ctk.CTkLabel(master= self.root,text="Bienvenido al videojuego de DOMINO")
        self.compu.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        self.botfichas = MyFrame(master=self.root,width=500)
        self.botfichas.place(relx=0.52, rely=0.8, anchor=tkinter.CENTER)
        
        self.jugc = ctk.CTkLabel(master=self.juego,text='')
        self.jugc.grid(row=2,column=2)
        self.jugc.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        #=====================> Botones de cada ficha del domino <====================
        
        self.TB0_0 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F0_0,text="",command=self.FB0_0)
        self.TB0_0.grid(row=0,column=0)
        
        self.TB0_1 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F0_1,text="",command=self.FB0_1)
        self.TB0_1.grid(row=0,column=1)
        
        self.TB0_2 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F0_2,text="",command=self.FB0_2)
        self.TB0_2.grid(row=0,column=2)
        
        self.TB0_3 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F0_3,text="",command=self.FB0_3)
        self.TB0_3.grid(row=0,column=3)
        
        self.TB0_4 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F0_4,text="",command=self.FB0_4)
        self.TB0_4.grid(row=0,column=4)
        
        self.TB0_5 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F0_5,text="",command=self.FB0_5)
        self.TB0_5.grid(row=0,column=5)
        
        self.TB0_6 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F0_6,text="",command=self.FB0_6)
        self.TB0_6.grid(row=0,column=6)
        
        self.TB1_1 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F1_1,text="",command=self.FB1_1)
        self.TB1_1.grid(row=1,column=0)
        
        self.TB1_2 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F1_2,text="",command=self.FB1_2)
        self.TB1_2.grid(row=1,column=1)
        
        self.TB1_3 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F1_3,text="",command=self.FB1_3)
        self.TB1_3.grid(row=1,column=2)
        
        self.TB1_4 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F1_4,text="",command=self.FB1_4)
        self.TB1_4.grid(row=1,column=3)
        
        self.TB1_5 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F1_5,text="",command=self.FB1_5)
        self.TB1_5.grid(row=1,column=4)
        
        self.TB1_6 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F1_6,text="",command=self.FB1_6)
        self.TB1_6.grid(row=1,column=5)
        
        self.TB2_2 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F2_2,text="",command=self.FB2_2)
        self.TB2_2.grid(row=1,column=6)
        
        self.TB2_3 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F2_3,text="",command=self.FB2_3)
        self.TB2_3.grid(row=2,column=0)
        
        self.TB2_4 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F2_4,text="",command=self.FB2_4)
        self.TB2_4.grid(row=2,column=1)
        
        self.TB2_5 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F2_5,text="",command=self.FB2_5)
        self.TB2_5.grid(row=2,column=2)
        
        self.TB2_6 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F2_6,text="",command=self.FB2_6)
        self.TB2_6.grid(row=2,column=3)
        
        self.TB3_3 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F3_3,text="",command=self.FB3_3)
        self.TB3_3.grid(row=2,column=4)
        
        self.TB3_4 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F3_4,text="",command=self.FB3_4)
        self.TB3_4.grid(row=2,column=5)
        
        self.TB3_5 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F3_5,text="",command=self.FB3_5)
        self.TB3_5.grid(row=2,column=6)
        
        self.TB3_6 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F3_6,text="",command=self.FB3_6)
        self.TB3_6.grid(row=3,column=0)
        
        self.TB4_4 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F4_4,text="",command=self.FB4_4)
        self.TB4_4.grid(row=3,column=1)
        
        self.TB4_5 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F4_5,text="",command=self.FB4_5)
        self.TB4_5.grid(row=3,column=2)
    
        self.TB4_6 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F4_6,text="",command=self.FB4_6)
        self.TB4_6.grid(row=3,column=3)
        
        self.TB5_5 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F5_5,text="",command=self.FB5_5)
        self.TB5_5.grid(row=3,column=4)
        
        self.TB5_6 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F5_6,text="",command=self.FB5_6)
        self.TB5_6.grid(row=3,column=5)
        
        self.TB6_6 = ctk.CTkButton(master= self.botfichas,width=70,height = 40,image=F6_6,text="",command=self.FB6_6)
        self.TB6_6.grid(row=3,column=6)
        
        #=================================================================================
        
        #================================Iniciamos el juego==============================
        self.root.update()
        self.compu.after(500)
        self.MulaSeis()
        self.DomiJu()
        self.root.update()
        self.botfichas.destroy()
        self.Combot.destroy()
        self.Tirbot1.destroy()
        self.Inicio = ctk.CTkButton(master= self.root,text= 'Inicio',command=self.Regresar)
        self.Inicio.place(relx=0.5,rely=0.6, anchor=tkinter.CENTER)
        self.Terminar = ctk.CTkButton(master= self.root,text= 'Terminar',command=self.Fin)
        self.Terminar.place(relx=0.5,rely=0.7, anchor=tkinter.CENTER)
        self.root.mainloop()
        
    def Fin(self):
        self.root.destroy()
    
    def DomiJu(self):
        while(self.final== False):
            self.root.update()
            self.compu.after(1000)
            self.compu.configure(text=('Turno '+str(len(self.Turnos))))
            if(len(self.ManoMK)==0):
                self.final=True
                self.win=0
                break
            if(self.Tiros==7):
                self.final=True
                self.win=1
                break
            
            if (self.Tuser==True):
                self.Tuser=True
                self.compu.after(1000)
                self.compu.configure(text=('Tu turno'))
                self.compu.after(1000)
                self.compu.configure(text=('Tiras o Comes'))
                self.Tirbot1 = ctk.CTkButton(master=self.root,text = "Tiro",width= 140,height=32,command= self.Tiro)
                self.Tirbot1.place(relx=0.2,rely=0.6)
                self.Combot = ctk.CTkButton(master=self.root,text = "Como",width= 140,height=32,command = self.Como)
                self.Combot.place(relx=0.7,rely=0.6)
                self.root.wait_variable(self.var)
                  
            elif(self.Tuser==False):
                self.root.update()
                self.compu.configure(text=('Mi turno'))
                self.compu.after(500)
                self.ACT=[self.TiroMK[0][0],self.TiroMK[-1][1]]    
                tiro2=self.SkyNet(self.ManoMK,self.TiroMK,self.ACT)
                if(tiro2==True):
                    self.Turnos.append(1)
                    self.Tuser=True
                elif(tiro2==False):
                    t4="""
                    No tengo TIRO Procedo a comer"""
                    self.compu.configure(text=t4)
                    self.root.update()
                    self.compu.after(1000)
                    self.comeMK()
                    self.cmm += 1
                    if(self.cmm==3):
                        self.final==True
                        self.win=1
                        self.Tuser=True
                        break
                    self.Tuser=False
            
        if(self.Tramposo ==True or self.win==0):
            self.compu.after(1000)
            self.compu.configure(text='GAME OVER Perdiste, mejor suerte la próxima')
        elif(self.win==1):
            self.compu.after(1000)
            self.compu.configure(text=('GAME OVER Felicidades ganaste!!!'))
    
    def comeMK(self):
        self.VC = ctk.CTkToplevel()
        self.VC.geometry("640x480")
        self.VC.title("Tomando foto")
        self.VC.configure(fg_color="#010101")
        self.VC.iconbitmap(os.path.join(carpeta_imagenes, "domino.ico"))
        self.labelVc = ctk.CTkLabel(master= self.VC,text="Cargando ....")
        self.labelVc.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        capt = ctk.CTkButton(master=self.VC,text="Tomar Foto",command = self.Capture)
        capt.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)
        self.cam = cv2.VideoCapture(1)
        self.varMK = False
        self.VC.update()
        self.labelVc.after(1000)
        self.labelVc.configure(text='Presiona el boton para tomar la foto')
        while self.varMK == False:
            self.ret, self.frame = self.cam.read()
            cv2.imshow('frame',self.frame)
            self.root.after(1)
            self.root.update_idletasks()
            self.root.update()

        
    def Capture(self):
        self.varMK = True
        io.imsave('foto.jpg', self.frame)
        self.cam.release()
        cv2.destroyAllWindows()
        self.image = io.imread('foto.jpg')
        self.Procesing()
        self.labelVc.configure(text=self.ManoMK)
        self.VC.update()
        self.VC.after(1000)
        self.VC.destroy()
     
    def Procesing(self):
        fic_gris = color.rgb2gray(self.image)
        fic_binario = (fic_gris > 0.34).astype(np.int16)
        sumC = np.sum(fic_binario,axis=0)
        sumF = np.sum(fic_binario,axis=1)
        corteC,corteF = self.corte(sumC,sumF)
        ficha_sep = self.Obj(corteC,corteF,fic_binario)
        for i in ficha_sep:
            fic = self.divficha(i)
            [filt1,filt2] = self.filtro(fic)
            [c1,c2,img1,img2] = self.circulos()
            c1 = self.Ratificar(c1)
            c2 = self.Ratificar(c2)
            self.ManoMK = self.contar(c1,c2,self.ManoMK)
    
    def corte(self,graf1,graf2):
        cortarC = []
        cortarF = []
        for i in range(len(graf1)-1):
            if (graf1[i] == 0 and graf1[i+1] != 0) or (graf1[i + 1] == 0 and graf1[i] != 0):
                cortarC.append(i)
        for i in range(len(graf2)-1):
            if (graf2[i] == 0 and graf2[i+1] != 0) or (graf2[i + 1] == 0 and graf2[i] != 0):
                cortarF.append(i)
        return cortarC,cortarF

    def Obj(self,corteC,corteF,ima):
        objetos = []
        umbral = 50
        for c in range(0,len(corteC),2):
            for f in range(0,len(corteF),2):
                if (corteF[f+1] - corteF[f] > umbral) and (corteC[c+1] - corteC[c] > umbral):
                    objetos.append(ima[corteF[f]:corteF[f+1],corteC[c]:corteC[c+1]]) 
        return objetos
 
    def divficha(self,ima):
        if ima.shape[0] > ima.shape[1]:
            corte = round(ima.shape[0]/2)
            ficha = [ima[:corte,:],ima[corte:,:]]
        else:
            corte = round(ima.shape[1]/2)
            ficha = [ima[:,:corte],ima[:,corte:]]
        return ficha
    
    def filtro(self,ficha):
        filt1_1 = morphology.binary_dilation(ficha[0])
        filt1_2 = morphology.binary_dilation(ficha[1])
        filt1_1 = morphology.binary_erosion(filt1_1)
        filt1_2 = morphology.binary_erosion(filt1_2)
        io.imsave("filt1.jpg",filt1_1)
        io.imsave("filt2.jpg",filt1_2)
        return filt1_1,filt1_2
    
    def circulos(self):
        img1 = cv2.imread("filt1.jpg")
        img2 = cv2.imread("filt2.jpg")
        img1 = cv2.medianBlur(img1, 3)
        img2 = cv2.medianBlur(img2, 3)
        img1 = cv2.GaussianBlur(img1, (5, 5), 0)
        img2 = cv2.GaussianBlur(img2, (5, 5), 0)
        gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        circles1 = cv2.HoughCircles(gray_img1, cv2.HOUGH_GRADIENT, 0.000001, 10,param1=70, param2=30, minRadius=0, maxRadius=0)
        circles2 = cv2.HoughCircles(gray_img2, cv2.HOUGH_GRADIENT, 0.000001, 10,param1=70, param2=30, minRadius=0, maxRadius=0)
        if circles1 is None:
            circles1 = circles1
        else:
            circles1 = np.uint16(np.around(circles1))
        if circles2 is None:
            circles2 = circles2
        else:
            circles2 = np.uint16(np.around(circles2))
        return circles1,circles2,gray_img1,gray_img2

    def Ratificar(self,circulos):
        if circulos is None:
            return circulos
        else:
            circs = circulos[0,:]
            for i in range(circs.shape[0]):
                if circs[i][2] >= 80 and circs[i][2]:
                    np.delete(circs, i)
        return circs
        
    def contar(self,c1,c2,fichas):
        if (c2 is None and c1 is None):
            fichas.append([0,0])
        elif c2 is None and len(c1) != 0:
            fichas.append([c1.shape[0],0])
        elif c1 is None and  len(c2) != 0:
            fichas.append([0,c2.shape[0]])
        else:
            fichas.append([c1.shape[0],c2.shape[0]])
        return fichas
    
    def SkyNet(self,hand,t,a):
        #print(ManoMK,'MANO')
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
                #print(d,'Hay la misma cantidad')
                MC=D
                #print(d,'usamos este valor')
                for k in inI:
                    man=hand[k]
                    if(man[0]==I):
                        nohandI.append(man[1])
                    else:
                        nohandI.append(man[0])
                for k in inD:
                    man=hand[k]
                    if(man[0]==D):
                        nohand.append(man[1])
                    else:
                        nohand.append(man[0])
                Mm=False
                DER=True
                IZ=False
                #print(nohand,'NohandD')
                #print(nohandI,'NohandI')
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
                for j in nohand:
                    conteo=0
                    for i in hand:
                        if(j==i[0] or j==i[1]):
                            conteo=conteo+1
                    CcD.append(conteo)
                #print(CcD,'CcD')
                McD=CcD.index(max(CcD))
                #print(McD,'MCD')
                #print(McI,'MCI')
                Mc=McD

        #------------------------------------------------------
            #print(nohand[Mc],'NohandMc')
            #print(MC,'MC')
           
            if IZ==True and DER==False:
                for i in inI:
                    if (hand[i][0]==nohand[Mc] and hand[i][1]==MC) or (hand[i][1]==nohand[Mc] and hand[i][0]==MC):
                        f=hand[i]
                        #print(f,'handi')
                        self.GAME(f)
                        #print(ManoMK[i],'Comprobar que sea la misma ficha')
                        self.ManoMK.pop(i)
                        break
            elif mula==True and DER==False and IZ==False:
                for i in inM:
                    if (hand[i][0]==nohand[Mc] and hand[i][1]==MC) or (hand[i][1]==nohand[Mc] and hand[i][0]==MC):
                        f=hand[i]
                        #print(f,'handi')
                        self.GAME(f)
                        #print(ManoMK[i],'Comprobar que sea la misma ficha')
                        self.ManoMK.pop(i)
                        break
            elif IZ==False and DER==True:
                for i in inD:
                    if (hand[i][0]==nohand[Mc] and hand[i][1]==MC) or (hand[i][1]==nohand[Mc] and hand[i][0]==MC):
                        f=hand[i]
                        #print(f,'handi')
                        self.GAME(f)
                        #print(ManoMK[i],'Comprobar que sea la misma ficha')
                        self.ManoMK.pop(i)
                        break
                
            else:
                if(McI>McD):
                    for i in inI:
                        if (hand[i][0]==McI and hand[i][1]==MC) or (hand[i][1]==McI and hand[i][0]==MC):
                            f=hand[i]                    
                            #print(f,'handi')
                            self.GAME(f)
                            #print(ManoMK[i],'Comprobar que sea la misma ficha')
                            self.ManoMK.pop(i)
                            break
                elif(McD>McI):
                    for i in inD:
                        if (hand[i][0]==McD and hand[i][1]==MC) or (hand[i][1]==McD and hand[i][0]==MC):
                            f=hand[i]
                            #print(f,'handi')
                            self.GAME(f)
                            #print(ManoMK[i],'Comprobar que sea la misma ficha')
                            self.ManoMK.pop(i)
                            break
                elif(McD==McI):
                    for i in inD:
                        if (hand[i][0]==McD and hand[i][1]==MC) or (hand[i][1]==McD and hand[i][0]==MC):
                            
                            f=hand[i]
                            #print(f,'handi')
                            self.GAME(f)
                            #print(ManoMK[i],'Comprobar que sea la misma ficha')
                            self.ManoMK.pop(i)
                            break
            #-----------------Acomodo------------------
            # print(f,'f')
            # print(I,'I')
            # print(D,'D')
        
        return c
    
    def Tiro(self):
        self.var.set(True)
        self.root.after(100, lambda: self.var.set(False))
        t4=self.TUserF()
        if t4==False:
            self.Tramposo=True
            self.win=0 
            self.Tuser=False
            self.final = True
        else:
            self.Tiros += 1
            self.Turnos.append(1)
            self.Tuser=False
        self.Tuser=False
    
    def Como(self):
        self.var.set(True)
        self.root.after(10, lambda: self.var.set(False))
        self.Tiros -= 1
        self.eat=self.comedorU()
        if self.eat==False:
            self.final=True
            self.win=0
        else:
            self.final=False
    
    def comedorU(self):
        self.Tirbot1.destroy()
        self.Combot.destroy()
        self.compu.configure(text='Comiste 1 Ficha')
        self.root.update()
        self.compu.after(2000)
        self.compu.configure(text='¿Necesitas comer mas?')
        self.BS2 = ctk.CTkButton(master=self.root,text='Si',command=self.S2)
        self.BS2.place(relx=0.2,rely=0.6)
        self.BN2 = ctk.CTkButton(master=self.root,text='No',command=self.N2)
        self.BN2.place(relx=0.7,rely=0.6)
        self.root.wait_variable(self.var1)
        return self.y
    
    def S2(self):
        self.BN2.destroy()
        self.BS2.destroy()
        self.var1.set(True)
        self.root.after(100, lambda: self.var1.set(False))
        self.compu.configure(text='Comiste 2 fichas')
        self.root.update()
        self.compu.after(1000)
        self.compu.configure(text='¿Necesitas comer mas?')
        self.Tiros -= 1
        self.BS3 = ctk.CTkButton(master=self.root,text='Si',command=self.S3)
        self.BS3.place(relx=0.2,rely=0.6)
        self.BN3 = ctk.CTkButton(master=self.root,text='No',command=self.N3)
        self.BN3.place(relx=0.7,rely=0.6)
        self.root.wait_variable(self.var2)
        
    def S3(self):
        self.BN3.destroy()
        self.BS3.destroy()
        self.var2.set(True)
        self.root.after(100, lambda: self.var2.set(False))
        self.compu.configure(text='Comiste 3 fichas')
        self.root.update()
        self.compu.after(1000)
        self.compu.configure(text='¿Necesitas comer mas?')
        self.Tiros -= 1
        self.BS4 = ctk.CTkButton(master=self.root,text='Si',command=self.S4)
        self.BS4.place(relx=0.2,rely=0.6)
        self.BN4 = ctk.CTkButton(master=self.root,text='No',command=self.N4)
        self.BN4.place(relx=0.7,rely=0.6)
        self.root.wait_variable(self.var3)
    
    def S4(self):
        self.BN4.destroy()
        self.BS4.destroy()
        self.var3.set(True)
        self.root.after(200, lambda: self.var3.set(False))
        self.var.set(True)
        self.root.after(200, lambda: self.var.set(False))
        self.y=False
        
    def N4(self):
        self.BN4.destroy()
        self.BS4.destroy()
        self.var.set(True)
        self.root.after(200, lambda: self.var.set(False))
        self.y=True
    
    def N3(self):
        self.BN3.destroy()
        self.BS3.destroy()
        self.var2.set(True)
        self.root.after(200, lambda: self.var2.set(False))
        self.var1.set(True)
        self.root.after(200, lambda: self.var1.set(False))
        self.y = True
    
    def N2(self):
        self.BN2.destroy()
        self.BS2.destroy()
        self.var1.set(True)
        self.root.after(200, lambda: self.var1.set(False))
        self.y = True
    
    def MulaSeis(self):
        for i in range(len(self.ManoMK)):
            if(self.ManoMK[i][0]==6 and self.ManoMK[i][1]==6 ):
                self.ManoMK.pop(i)
                T=[6,6]
                self.TiroMK.append(T)
                self.compu.after(1000)
                self.compu.configure(text=self.tirada)
                self.jugc.configure(text=self.TiroMK)
                self.Turnos.append(1)
                self.seises=False
                self.Tuser=True
                break
        if(self.seises==True):
            self.compu.after(1000)
            self.compu.configure(text='¿Tienes la mula del 6?')
            self.BS = ctk.CTkButton(master=self.root,text='Si',command=self.S)
            self.BS.place(relx=0.2,rely=0.6)
            self.BN = ctk.CTkButton(master=self.root,text='No',command=self.N)
            self.BN.place(relx=0.7,rely=0.6)
            self.root.wait_variable(self.var)
        self.Add=4     
        self.win=2
        self.final=False
        if(self.seises==False):
            self.Tuser=True
        if self.Tramposo==True:
            self.final=True
            self.win=0
        self.cmm=0
            
    def S(self):
        T=[6,6]
        self.var.set(True)
        self.root.after(200, lambda: self.var.set(False))
        self.TiroMK.append(T)
        self.Tiros += 1
        self.compu.after(1000)
        self.compu.configure(text=self.tirada)
        self.jugc.configure(text=self.TiroMK)
        self.Turnos.append(1)
        self.Tuser=False
        self.BS.destroy()
        self.BN.destroy()
            
    def N(self):
        self.BS.destroy()
        self.BN.destroy()
        self.sM=self.SinMula(self.ManoMK)
        if(self.sM[0]>=0 and self.sM[0]<10):
            sM1=self.sM[0]
            self.iz=self.ManoMK[sM1][0]
            self.der=self.ManoMK[sM1][1]
            self.compu.after(1000)
            self.compu.configure(text='¿Tienes alguna mula?')
            self.BS1 = ctk.CTkButton(master=self.root,text='Si',command=self.S1)
            self.BS1.place(relx=0.2,rely=0.6)
            self.BN1 = ctk.CTkButton(master=self.root,text='No',command=self.N1)
            self.BN1.place(relx=0.7,rely=0.6)
            self.root.wait_variable(self.var)
        else:
            t3="""
            No tengo MULAS Tira una MULA o cualquier otra ficha"""
            self.compu.after(1000)
            self.compu.configure(text=t3)
            t4=self.TUser()
            if t4==False:
                self.Tramposo=True
            else:
                self.Tiros+=1
                self.Turnos.append(1)
    
    def TUser(self):
        self.root.wait_variable(self.var)
        T= self.F
        c=self.checador(self.ManoMK, self.TiroMK, T)
        if c==False:
            c=False
        else:
            self.GAME(T)
            c=True
        return c
    
    def TUserF(self):
        self.root.wait_variable(self.varFicha)
        tu= self.F
        tuF=self.checador(self.ManoMK,self.TiroMK,tu)
        if (tuF==False):
            c=False
        else:
            T=[tu[0],tu[1]]
            self.GAME(T)
            c=True
        return c
    
    def S1(self):
        self.var.set(True)
        self.root.after(200, lambda: self.var.set(False))
        self.BS1.destroy()
        self.BN1.destroy()
        t4=self.TUserMULA(self.iz,self.der)
        if (t4==False):
            self.Tramposo=True
        else:   
            self.Turnos.append(1)
            self.Tiros += 1
            self.Tuser=False
        
    def N1(self):
        self.var.set(True)
        self.root.after(1200, lambda: self.var.set(False))
        self.BS1.destroy()
        self.BN1.destroy()
        T=[self.sM[1],self.sM[1]]
        self.TiroMK.append(T)
        self.compu.after(1000)
        self.compu.configure(text=self.tirada)
        self.jugc.configure(text=self.TiroMK)
        self.Tuser=True
    
    def TUserMULA(self,iz,der):
        self.root.wait_variable(self.varFicha)
        tiroU1=self.F[0]
        tiroU2=self.F[1]
        X=self.checador(self.ManoMK,self.TiroMK, [tiroU1,tiroU2])

        if(tiroU1>iz and tiroU2>der and X==True):
            T=[tiroU1,tiroU2]
            self.GAME([tiroU1,tiroU2])
            a=True
            self.Tuser=False
        elif(X==False):
            a=False
        else:
            self.compu.configure(text='Te regreso tu ficha tengo una mula mayor')
            T=[iz,der]
            self.GAME(T)
            self.Turnos.append(1)
            self.Tuser=True
            a=True
        return a
        
    def checador(self,manoM, manoT, mano):
        n1=mano[0]
        n2=mano[1]
        m1="""
        DESCALIFICADO POR TRAMPOS@ ESA FICHA SE ENCUENTRA EN MI MAZO
        """
        m2="""
        DESCALIFICADO POR TRAMPOS@ ESA FICHA YA FUE JUGADA
        """
        mano=True
        for i in range(len(self.ManoMK)):
            if(manoM[i][0]==n1 and manoM[i][1]==n2 ):
                self.compu.configure(text=m1)
                self.root.update()
                self.compu.after(1000)
                mano=False
                break
            elif(manoM[i][1]==n1 and manoM[i][0]==n2 ):
                self.compu.configure(text=m1)
                self.root.update()
                self.compu.after(1000)
                mano=False
                break
        for i in range(len(self.TiroMK)):
            if(manoT[i][0]==n1 and manoT[i][1]==n2 ):
                self.compu.configure(text=m2)
                self.root.update()
                self.compu.after(1000)
                mano=False
                break
            elif(manoT[i][1]==n1 and manoT[i][0]==n2 ):
                self.compu.configure(text=m2)
                self.root.update()
                self.compu.after(1000)
                mano=False
                break
        return mano
    
    def GAME(self,f):
        if(len(self.TiroMK)>0):
            I=self.TiroMK[0][0]
            D=self.TiroMK[-1][1]
            if (f[0]==I and f[1]!=D):
                self.TiroMK.insert(0,[f[1],f[0]])
            elif (f[1]==I and f[0]!=D):    
                self.TiroMK.insert(0,[f[0],f[1]])
            elif (f[0]==D and f[1]!=I):    
                self.TiroMK.append([f[0],f[1]])
            elif (f[1]==D and f[0]!=I):    
                self.TiroMK.append([f[1],f[0]])
            elif (f[1]==D and f[0]==I):    
                self.TiroMK.append([f[1],f[0]])
            elif (f[0]==D and f[0]==I):    
                self.TiroMK.append([f[0],f[1]])
            elif (f[1]==D and f[1]==I):    
                self.TiroMK.append([f[1],f[0]])
        else:
            self.TiroMK.append(f)
        self.compu.after(1000)
        self.compu.configure(text=self.tirada)
        self.jugc.configure(text=self.TiroMK)
        return
    
    def SinMula(self,mano):
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
        
    def Regresar(self):
        self.root.destroy()
        In = Inicio()
       
    def FB0_0(self):
        self.F = [0,0]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB0_1(self):
        self.F = [0,1]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB0_2(self):
        self.F = [0,2]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB0_3(self):
        self.F = [0,3]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB0_4(self):
        self.F = [0,4]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB0_5(self):
        self.F = [0,5]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB0_6(self):
        self.F = [0,6]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB1_1(self):
        self.F = [1,1]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB1_2(self):
        self.F = [1,2]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB1_3(self):
        self.F = [1,3]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB1_4(self):
        self.F = [1,4]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB1_5(self):
        self.F = [1,5]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB1_6(self):
        self.F = [1,6]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB2_2(self):
        self.F = [2,2]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB2_3(self):
        self.F = [2,3]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB2_4(self):
        self.F = [2,4]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB2_5(self):
        self.F = [2,5]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB2_6(self):
        self.F = [2,6]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB3_3(self):
        self.F = [3,3]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB3_4(self):
        self.F = [3,4]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB3_5(self):
        self.F = [3,5]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB3_6(self):
        self.F = [3,6]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB4_4(self):
        self.F = [4,4]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB4_5(self):
        self.F = [4,5]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB4_6(self):
        self.F = [4,6]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB5_5(self):
        self.F = [5,5]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB5_6(self):
        self.F = [5,6]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
        
    def FB6_6(self):
        self.F = [6,6]
        self.varFicha.set(True)
        self.root.after(10, lambda: self.varFicha.set(False))
Ficha = [[1,1],[2,4],[3,3],[5,2],[0,5],[6,4],[3,3]]   
a = Juegos(Ficha)

