from tkinter import *
import cv2
import numpy as np
from datetime import date
from datetime import datetime

def rojo():
    
    captura=cv2.VideoCapture(0)
    
    #rango del color 
    #primer rango
    rojobajo = (0, 100, 20) 
    rojoAlto = (8, 255, 255)

    #segundo rango
    rojoBajo1= (175, 100, 20)
    rojoAlto1= (179, 255, 255)

    while True:
        ret,imagen=captura.read()
        if ret==True:
            imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            maskRojo1 = cv2.inRange(imagenHSV, rojobajo, rojoAlto) #buscar el rango del color
            maskRojo2 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
            maskRojo = cv2.add(maskRojo1, maskRojo2) #como son dos rangos, une los dos en uno solo
            maskRojo3 = cv2.bitwise_and(imagen, imagen, mask= maskRojo)
            cv2.imshow('imagen',imagen)
            #cv2.imshow('maskRojo', maskRojo) #visualizacion muestra el color en blanco y el resto en negro
            cv2.imshow('maskRojo3', maskRojo3) #muestra el color y el resto en negro

        if cv2.waitKey(1) &  0xFF == ord('r'): # waitkey variar para reproduccion rapida o lenta
            break
    

    captura.release()
    #salida.release()
    cv2.destroyAllWindows

  

#----------------------------------------------------------------

def azul():

    captura=cv2.VideoCapture(0)

    azulbajo = (100, 100, 20) 
    azulAlto = (130, 255, 255)

    while True:
        ret,imagen=captura.read()
        if ret==True:
            imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            maskazul = cv2.inRange(imagenHSV, azulbajo, azulAlto) 
            maskazul2 = cv2.bitwise_and(imagen, imagen, mask= maskazul)
            
            cv2.imshow('imagen',imagen)
            #cv2.imshow('maskazul', maskazul) 
            cv2.imshow('maskazul2', maskazul2) 
            
        if cv2.waitKey(1) &  0xFF == ord('b'): 
            break
    

    captura.release()
    cv2.destroyAllWindows
   

#------------------------------------------------------------------------------------------------------------------------

def amarillo():

    captura=cv2.VideoCapture(0)

    amaribajo = (15, 100, 20) 
    amariAlto = (40, 255, 255)

    while True:
        ret,imagen=captura.read()
        if ret==True:
            imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            maskamari = cv2.inRange(imagenHSV, amaribajo, amariAlto) 
            maskamari2 = cv2.bitwise_and(imagen, imagen, mask= maskamari)
           
            cv2.imshow('imagen',imagen)
            #cv2.imshow('maskamari', maskamari) 
            cv2.imshow('maskamari2', maskamari2) 
            
        if cv2.waitKey(1) &  0xFF == ord('y'): 
            break
    

    captura.release()
    cv2.destroyAllWindows
  

#----------------------------------------------------------------------------------------------------


def todos():
    captura=cv2.VideoCapture(0)

    rojobajo = (0, 100, 20) 
    rojoAlto = (8, 255, 255)
    rojoBajo1=(175, 100, 20)
    rojoAlto1=(179, 255, 255)

    azulbajo = (100, 100, 20) 
    azulAlto = (130, 255, 255)

    amaribajo = (15, 100, 20) 
    amariAlto = (40, 255, 255)

    while True:
        ret,imagen=captura.read()
        if ret==True:
            imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
            
            maskRojo1 = cv2.inRange(imagenHSV, rojobajo, rojoAlto) 
            maskRojo2 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
            maskRojo = cv2.add(maskRojo1, maskRojo2) 
            
            maskazul = cv2.inRange(imagenHSV, azulbajo, azulAlto) 
            maskamari = cv2.inRange(imagenHSV, amaribajo, amariAlto) 
            maskazulamari = cv2.add(maskazul, maskamari)
           

            masktodos = cv2.add(maskRojo, maskazulamari) 
            masktodos1 = cv2.bitwise_and(imagen, imagen, mask= masktodos)
           
            cv2.imshow('imagen',imagen)
            #cv2.imshow('masktodos', masktodos) 
            cv2.imshow('masktodos1', masktodos1) 
            
        if cv2.waitKey(1) &  0xFF == ord('t'): 
            break
    

    captura.release()
    cv2.destroyAllWindows


global ventana
ventana=Tk()
ventana.title('openCV')
ventana.geometry('750x300')
ventana.configure(bg='#66EB54')
now=date.today()
img=PhotoImage(file="fondo1.png")


anuncio=Label(ventana, text=now, font=('Arial',15),fg='blue')
anuncio.configure(bg='#66EB54')
titulo=Label(ventana, text='DETECTOR DE COLORES PRIMARIOS', font=('Arial',15),fg='black')
titulo.configure(bg='#66EB54')
fondo=Label(ventana, image=img)




boton1= Button(ventana, text='COLOR ROJO',font=('Arial',15),height = 1, width = 20,command=rojo)
boton1.configure(bg="red")
boton2= Button(ventana, text='COLOR AZUL',font=('Arial',15),height = 1, width = 20,command=azul)
boton2.configure(bg="blue")
boton3= Button(ventana, text='COLOR AMARILLO',font=('Arial',15),height = 1, width = 20,command=amarillo)
boton3.configure(bg="yellow")
boton4= Button(ventana, text='COLORES PRIMARIOS',font=('Arial',15),height = 1, width = 20,command=todos)

boton5= Button(ventana, text='salir',font=('Arial',15),command=lambda:ventana.destroy())

anuncio.grid(row= 0, column= 4)
titulo.grid(row= 0, column=2)
fondo.place(x=235,y=33)



boton1.grid(row=3, column=1,pady=6)
boton2.grid(row=4, column=1,pady=6)
boton3.grid(row=5, column=1,pady=6)
boton4.grid(row=6, column=1,pady=6)
boton5.grid(row=7, column=4,pady=6)
    

ventana.mainloop()

  

    
