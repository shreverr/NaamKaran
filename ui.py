import customtkinter

import tkinter

#main window named "root"

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

NKWindow = customtkinter.CTk()
NKWindow.geometry("928x522")
NKWindow.title("Naam Karan")

T1 = customtkinter.CTkLabel(NKWindow, text = "Welcome to the Program")    # T1 - 1st Text
T1.pack()

NKWindow.mainloop()
