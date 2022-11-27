
import customtkinter

import tkinter

#main window named "NKWind"

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

NKWind = customtkinter.CTk()
NKWind.geometry("928x522")
NKWind.title("Naam Karan")
NKWind.iconbitmap("NaamKaran.ico")

# L1 = customtkinter.CTkLabel(NKWind, text ="Welcome to the Program")    # L1 - 1st Text
# L1.pack()

F1 = customtkinter.CTkFrame(master=NKWind)
F1.pack(pady=10, padx=60, fill="both", expand = True)

L2 = customtkinter.CTkLabel(master=F1, text = "First Line",  justify=tkinter.LEFT)
L2.pack(pady=12, padx=10)

L3 = customtkinter.CTkLabel(master=F1, text = "Second Line",  justify=tkinter.LEFT)
L3.pack(pady=12, padx=10)

NKWind.mainloop()
