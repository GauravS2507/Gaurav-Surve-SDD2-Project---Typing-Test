#Basic Import Functions
import tkinter as tk
import customtkinter
from tkinter import *
from tkinter import messagebox
import random
import keyboard
import time

#Place Holder Variables
x = 0

#Pop Up-Window - Begin Touch Type Helper
root = customtkinter.CTk()
root.geometry("450x600")
root.title("Touch Typing Helper")
root.frame1 = customtkinter.CTkFrame(root, width=400, height=500)
root.frame1.grid(row=0, column=0, padx=30, pady=30)



#Defining Commands
def New_window():    #From Open Window --> Main Window
    global x
    #Destroy the first window when Begin is pressed
    if x==0:
        x=1
        root.destroy()



#Labels Used
Welcome_TTH = customtkinter.CTkLabel(root, text="Welcome to the Touch Type Helper")

#Buttons
Begin_TTH = customtkinter.CTkButton(root, text = "Begin", command=New_window,  )
Settings = customtkinter.CTkButton(root, text = "Settings⚙️")
Credits = customtkinter.CTkButton(root, text = "Credits")

#Widget Positioning
Welcome_TTH.grid(row = 0, column = 0, padx=0, pady=0)
Begin_TTH.grid(row=2, column=0, padx=0, pady=0)
Settings.grid()
Credits.grid()







root.mainloop()