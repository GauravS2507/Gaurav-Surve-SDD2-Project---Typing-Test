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

#Defining Commands
def New_window():    #From Open Window --> Main Window
    global x, frame1
    #Clearing Frame
    if x==0:
        x=1
        for widgets in frame1.winfo_children(): #Emptying out frame 
            widgets.destroy()
            root.geometry("1000x600")
            frame1 = customtkinter.CTkFrame(root, width=900, height=500)
            frame1.grid(row=0, column=0, padx=20, pady=30)

def settings():     #Command for settings button
    settings_window = customtkinter.CTkToplevel(root)
    settings_window.title("Settings - Touch Typing Helper - Gaurav Surve")
    settings_window.geometry("500x300")
    settings_window.resizable(False, False)
    frame2 = customtkinter.CTkFrame(settings_window, width = 450, height = 250) #Settings Pop-up window frame
    frame2.grid(row=0, column=0, padx=25, pady=25)

    

        


#Pop Up-Window - Begin Touch Type Helper
root = customtkinter.CTk()
root.geometry("450x350")
root.title("Touch Typing Helper - Gaurav Surve")
root.resizable(False, False)


# Create a frame for main window
frame1 = customtkinter.CTkFrame(root, width=400, height=500, border_width = 10, border_color = "#13141F")
frame1.grid(row=0, column=0, padx=20, pady=30, )

# Labels Used
Welcome_TTH = customtkinter.CTkLabel(frame1, text="Welcome to the Touch Type Helper", font=("Work Sans", 24), fg_color="#000435", corner_radius=100)
Welcome_TTH.grid(row=0, column=0, padx=0, pady=60)

# Buttons
Begin_TTH = customtkinter.CTkButton(frame1, text="Begin", font=("Arial", 16), fg_color="#282E78", command = New_window)
Begin_TTH.grid(row=1, column=0, padx=0, pady=10)

Settings = customtkinter.CTkButton(frame1, text="Settings⚙️", font=("Arial", 16), fg_color="#282E78", command = settings)
Settings.grid(row=2, column=0, padx=0, pady=10)

Credits = customtkinter.CTkButton(frame1, text="Credits", font=("Arial", 16), fg_color="#282E78")
Credits.grid(row=3, column=0, padx=0, pady=10)

#Themes
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


root.mainloop()