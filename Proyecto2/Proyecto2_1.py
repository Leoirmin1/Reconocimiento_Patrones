# -*- coding: utf-8 -*-
"""
Created on Thu May 25 20:05:50 2023

@author: ASUS
"""

from keras.models import load_model
import numpy as np
from python_speech_features import mfcc
from python_speech_features import logfbank
import pyaudio as pad
import wave
from scipy.io import wavfile
import sklearn as sk
import noisereduce as nr
# Cargamos el modelo de la neurona elaborado con keras
model = load_model('Det.h5')

def extract_mfcc(full_audio_path):
    sample_rate,data = wavfile.read(full_audio_path)
    sample_rater,datar = wavfile.read('ruido.wav')
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
    if len(datar.shape) > 1:
        datar = np.mean(datar, axis=1)
    data = nr.reduce_noise(data,sample_rate,y_noise=datar,prop_decrease = 1.0)
    mfcc_features = mfcc(data, sample_rate, nfft=2048, preemph=0.97, numcep=13, ceplifter=100, winstep=0.005, nfilt=100)
    return mfcc_features




def Grab_Audio():
    chunk = 1024                         # Grabado en paquetes de 512 muestras
    sample_format = pad.paInt16     # Resolucion de 16 bits
    channels = 2
    fs = 44100                           # Velocidad de muestreo 8000 por segundo
    seconds = 1.5                       # Tiempo de grabacion - segundos
    audio_obj = pad.PyAudio()       # Crear el objeto de audio
    filename = 'prueba.wav'
    print(filename)
    input('Click tecla')
    print('Inicia Grabación')
    stream = audio_obj.open(format= sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)
    tramas = []
    audio = []
    for i in range(0, int(fs/chunk*seconds)):
        datos = stream.read(chunk)
        tramas.append(datos)
        audio.append(np.frombuffer(datos,dtype=np.int16))
    stream.stop_stream()
    stream.close()
    print('Termina grabacion')
    #-----------------------------------------------------------------------
    wf = wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio_obj.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(tramas))
    wf.close
    audio_obj.terminate()
    audio_obj = pad.PyAudio()       # Crear el objeto de audio
    filename = 'ruido.wav'
    stream = audio_obj.open(format= sample_format,channels=channels,rate=fs,frames_per_buffer=chunk,input=True)
    tramas = []
    audio = []
    for i in range(0, int(fs/chunk*seconds)):
        datos = stream.read(chunk)
        tramas.append(datos)
        audio.append(np.frombuffer(datos,dtype=np.int16))
    stream.stop_stream()
    stream.close()
    #-----------------------------------------------------------------------
    wf = wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio_obj.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(tramas))
    wf.close
    audio_obj.terminate()


labels = ['go','links','rechs','zuruck']
    
s = 1
while (s == 1):
    
    Grab_Audio()
    features = extract_mfcc("prueba.wav")
    features = features.reshape(1, features.shape[0], features.shape[1])
    # Utilizar el modelo para predecir la etiqueta del audio grabado
    prediction = model.predict(features)
    
    # Decodificar la predicción
    predicted_label = labels[np.argmax(prediction)]
    
    print("La etiqueta predecida es: ", predicted_label)
    
    s = int(input("""¿Quieres seguir?
                  1) Si
                  2) No
                  """))
    
