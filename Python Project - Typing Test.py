#Basic Import Functions
import tkinter as tk
import customtkinter as ctk
import PIL.Image
from tkinter import *
from tkinter import messagebox
import random
import keyboard
import time
from pathlib import Path


#Place Holder Variables
x= 0

#Defining Commands
def New_window():    #From Open Window --> Main Window
    global x, frame1
    #Clearing Frame
    if x==0 :
        x= 1
        for widget in frame1.winfo_children(): #Emptying out frame 
            widget.place_forget()
            root.geometry("1400x700")
            frame1 = ctk.CTkFrame(root, width=1300, height=600)
            frame1.pack(expand = True, fill = "both")
            frame3 = ctk.CTkFrame(frame1, width = 1200, height = 200)
            frame3.place(relx = 0.5, rely = 0.9, anchor = "s")
            

def settings():     #Command for settings button
    settings_window = ctk.CTkToplevel(root)
    settings_window.title("Settings - Touch Typing Helper - Gaurav Surve")
    settings_window.geometry("500x300")
    #Frame 2 Setting
    frame2 = ctk.CTkFrame(settings_window, width = 450, height = 250) #Settings Pop-up window frame
    frame2.grid(row=0, column=0, padx=25, pady=25)

#Pop Up-Window - Begin Touch Type Helper
root = ctk.CTk()
root.geometry("450x350")
root.title("Touch Typing Helper - Gaurav Surve")

#Frame1
frame1 = ctk.CTkFrame(root,width=400, height=500, border_width = 10, border_color = "#13141F")
frame1.pack(expand = True, fill = "both")
# Labels Used
Welcome_TTH = ctk.CTkLabel(frame1, text="Welcome to the Touch Type Helper", font=("Work Sans", 24), fg_color="#000435", corner_radius=100)
Welcome_TTH.place(relx = 0.5, rely = 0.2, anchor = "c")

# Buttons
Begin_TTH = ctk.CTkButton(frame1, text="Begin", font=("Arial", 16), fg_color="#282E78", command = New_window)
Begin_TTH.place(relx = 0.5, rely = 0.4, anchor = "c")

Settings = ctk.CTkButton(frame1, text="Settings⚙️", font=("Arial", 16), fg_color="#282E78", command = settings)
Settings.place(relx = 0.5, rely = 0.5, anchor = "c")

Credits = ctk.CTkButton(frame1, text="Credits", font=("Arial", 16), fg_color="#282E78")
Credits.place(relx = 0.5, rely = 0.6, anchor = "c")

#Themes
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


root.mainloop()