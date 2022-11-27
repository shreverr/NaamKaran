
import customtkinter

import tkinter

# Main window named "NKWind"

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

NKWind = customtkinter.CTk()
NKWind.geometry("928x522")
NKWind.title("Naam Karan")
NKWind.iconbitmap("NaamKaran.ico")

F1 = customtkinter.CTkFrame(master=NKWind)    # F1 - Main Frame
F1.pack(pady=10, padx=60, fill="both", expand = True)

L1 = customtkinter.CTkLabel(master=F1, text = "First Line",  justify=tkinter.LEFT)
L1.pack(pady=12, padx=10)

L2 = customtkinter.CTkLabel(master=F1, text = "Second Line",  justify=tkinter.LEFT)
L2.pack(pady=12, padx=10)

NKWind.mainloop()
