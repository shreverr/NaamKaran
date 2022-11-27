
import customtkinter

import tkinter

# Main window named "NKWind"

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

NKWind = customtkinter.CTk()
NKWind.geometry("928x522")
NKWind.title("NaamKaran")
NKWind.iconbitmap("NaamKaran.ico")

# F1 = customtkinter.CTkFrame(master=NKWind)    # F1 - Main Frame
# F1.pack(pady=10, padx=60, fill="both", expand = True)
#
# L1 = customtkinter.CTkLabel(master=F1, text="First Line",  justify=tkinter.LEFT)
# L1.grid(row=0, column=1)
#
# L2 = customtkinter.CTkLabel(master=F1, text="Second Line",  justify=tkinter.LEFT)
# L2.pack(pady=12, padx=10)
# SearchTextB = customtkinter.CTkTextbox(master = F1, height=20, width=50,fg_color="#DEACF5")
# SearchTextB.pack()

# ============ create two frames ============
# 1st frame 3X2
NKWind.grid_columnconfigure(1, weight=1)
NKWind.grid_rowconfigure(0, weight=1)

NKWind.frame_right = customtkinter.CTkFrame(master=NKWind)
NKWind.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

NKWind.frame_left = customtkinter.CTkFrame(master=NKWind, width=300, corner_radius=0)
NKWind.frame_left.grid(row=0, column=0, sticky="nsw")

NKWind.entry = customtkinter.CTkEntry(master=NKWind.frame_left,width=120,placeholder_text="Search for")
NKWind.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

NKWind.mainloop()
