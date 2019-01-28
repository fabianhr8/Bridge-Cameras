import urllib.request
from tkinter import *
from PIL import Image, ImageTk
import time
import psutil
import numpy as np
import cv2
import os

bridge = Tk()
bridge.title('Open Bridge')
bridge.geometry('300x100')


camerasLinks = open("bridgeCameras.txt", "r")     #read cameras file

lineNum = []
i = 0

global zara1Img
global zara2Img


for line in camerasLinks:       # Orginize each line on the file
    lineNum.append(line)
    i += 1

zaragoza1 = lineNum[6]        # Assign links to their corresponding bridges
zaragoza2 = lineNum[7]
centro1 = lineNum[10]
centro2 = lineNum[11]
express1 = lineNum[16]
express2 = lineNum[17]

######### download Zaragoza images and display them
def zaragoza():
    zaraWindow = Toplevel()
    zaraWindow.title('Zaragoza')

    urllib.request.urlretrieve(zaragoza1, 'fotoZara1.jpg')
    urllib.request.urlretrieve(zaragoza2, 'fotoZara2.jpg')

    zara1TkImg = ImageTk.PhotoImage(Image.open('fotoZara1.jpg'))
    zara2TkImg = ImageTk.PhotoImage(Image.open('fotoZara2.jpg'))

    zara1Img = Label(zaraWindow, image = zara1TkImg)
    zara1Img.image = zara1TkImg
    zara1Img.grid(row = 0, column = 0)

    zara2Img = Label(zaraWindow, image = zara2TkImg)
    zara2Img.image = zara2TkImg
    zara2Img.grid(row = 0, column = 1)

    exitZara = Button(zaraWindow, text = 'Close', command = zaraWindow.destroy)
    exitZara.grid(row = 1, column = 0, columnspan = 2)

######### download Centro images and display them
def centro():
    centroWindow = Toplevel()
    centroWindow.title('Centro')

    urllib.request.urlretrieve(centro1, 'fotoCentro1.jpg')
    urllib.request.urlretrieve(centro2, 'fotoCentro2.jpg')

    centro1TkImg = ImageTk.PhotoImage(Image.open('fotoCentro1.jpg'))
    centro2TkImg = ImageTk.PhotoImage(Image.open('fotoCentro2.jpg'))

    centro1Img = Label(centroWindow, image = centro1TkImg)
    centro1Img.image = centro1TkImg
    centro1Img.grid(row = 0, column = 0)

    centro2Img = Label(centroWindow, image = centro2TkImg)
    centro2Img.image = centro2TkImg
    centro2Img.grid(row = 0, column = 1)

    exitCentro = Button(centroWindow, text = 'Close', command = centroWindow.destroy)
    exitCentro.grid(row = 1, column = 0, columnspan = 2)

######### download Express images and display them
def express():
    expWindow = Toplevel()
    expWindow.title('Express')

    urllib.request.urlretrieve(express1, 'fotoExp1.jpg')
    urllib.request.urlretrieve(express2, 'fotoExp2.jpg')

    exp1TkImg = ImageTk.PhotoImage(Image.open('fotoExp1.jpg'))
    exp2TkImg = ImageTk.PhotoImage(Image.open('fotoExp2.jpg'))

    exp1Img = Label(expWindow, image = exp1TkImg)
    exp1Img.image = exp1TkImg
    exp1Img.grid(row = 0, column = 0)

    exp2Img = Label(expWindow, image = exp2TkImg)
    exp2Img.image = exp2TkImg
    exp2Img.grid(row = 0, column = 1)

    exitExp = Button(expWindow, text = 'Close', command = expWindow.destroy)
    exitExp.grid(row = 1, column = 0, columnspan = 2)



########## Main function
#def main():

label1 = Label(bridge, text = 'Choose your bridge:')
label1.grid(row = 0, columnspan = 3)
zaragoza_button = Button(bridge, text = 'Zaragoza', command=zaragoza)
zaragoza_button.grid(row = 1, column = 0)
centro_button = Button(bridge, text = 'Centro', command=centro)
centro_button.grid(row = 1, column = 1)
express_button = Button(bridge, text = 'Express', command=express)
express_button.grid(row = 1, column = 2)
exit_button = Button(bridge, text = 'Exit', command = bridge.destroy)
exit_button.grid(row = 2, columnspan = 3)
#bridge.bind("<Escape>", bridge.destroy)        #

bridge.mainloop()






