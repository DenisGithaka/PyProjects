# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 20:09:09 2022

@author: Gdams
"""
from tkinter import *
from gtts import gTTS
from playsound import playsound as pls
import os

root = Tk()
root.geometry('350x500')
root.configure(bg="ghost white")
root.title("Deesc - Text to Speech")

Label(root, text = 'TEXT TO SPEECH', font = 'arial 20 bold', bg = 'white smoke').pack()
Label(text ="Deesc Gdams", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
msg = StringVar()
Label(root, text = 'Enter Text', font = 'arial 12 bold', bg = 'white smoke').place(x=21, y=60)
entry_field = Entry(root, textvariable = msg, width = '50')
entry_field.place(x=20, y=100)


def text2speech():
    Message = entry_field.get()
    Speech = gTTS(text = Message)
    Speech.save("Converted.mp3")
    os.system("Converted.mp3")

    
def Exit():
    root.destroy()
    
def Ret():
    msg.set('')
    
Button(root, text = 'PLAY', font = 'arial 14 bold',command= text2speech, width = 5 , bg = 'royal blue1', activebackground = 'sky blue').place(x=25, y=200)
Button(root, text = 'EXIT', font = 'arial 14 bold',command= Exit, width = 5 , bg = 'OrangeRed1', activebackground = 'sky blue').place(x=140, y=200)
Button(root, text = 'RESET', font = 'arial 14 bold',command= Ret, width = 5).place(x=255, y=200)

root.mainloop()
#%%
ps("Converted.mp3")