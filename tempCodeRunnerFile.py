#Labels Used
Welcome_TTH = Label(root, text="Welcome to the Touch Type Helper", borderwidth=7, relief="ridge")

#Buttons
Begin_TTH = Button(root, text = "Begin", command=New_window, borderwidth=7 )
Settings = Button(root, text = "Settings⚙️")

#Positioning Widgets
Welcome_TTH.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
Welcome_TTH.config(bg="lightblue")
Begin_TTH.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
Begin_TTH.config(bg="lightblue")
Settings.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
Settings.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
