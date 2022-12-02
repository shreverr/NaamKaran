
import customtkinter

from tkinter import *
#============Main window named "NKWind"============

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#============Window Dimensions============
NKWind = customtkinter.CTk()
NKWind.geometry("1080x522")
NKWind.title("NaamKaran")

#============Icon============
NKWind.iconbitmap("NaamKaran.ico")

# 1st frame 3X2
NKWind.grid_columnconfigure(1, weight=1)
NKWind.grid_rowconfigure(0, weight=1)

NKWind.frame_right = customtkinter.CTkFrame(master=NKWind)
NKWind.frame_right.grid(row=0, column=1, sticky="nswe",padx=5,pady=10)

NKWind.frame_left = customtkinter.CTkFrame(master=NKWind)
NKWind.frame_left.grid(row=0, column=0, sticky="nswe", padx=5, pady=10)

# configure grid layout (1x11)
NKWind.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
NKWind.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
NKWind.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
NKWind.frame_left.grid_rowconfigure(11, minsize=10)

#============Prefix Entry============
NKWind.entry = customtkinter.CTkEntry(master=NKWind.frame_left,width=250,height=40,placeholder_text="Prefix")
NKWind.entry.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky="we")

#============Suffix Entry============
NKWind.entry = customtkinter.CTkEntry(master=NKWind.frame_left,width=250,height=40,placeholder_text="Suffix")
NKWind.entry.grid(row=1, column=0, columnspan=2, pady=20, padx=20, sticky="we")

#============Sort By Drop Down============
NKWind.Sort = customtkinter.CTkOptionMenu(master=NKWind.frame_left, values=["Sort By","Date Modified", "Ascending", "Descending"])
NKWind.Sort.grid(row=2, column=0, pady=10, padx=20, sticky="w")

#============Date and Time Drop Down============
NKWind.Date_Time = customtkinter.CTkOptionMenu(master=NKWind.frame_left, values=["Date and Time", "DDMMYYYY", "YYYYMMDD", "YYYY", "YY", "MM","DD"])
NKWind.Date_Time.grid(row=3, column=0, pady=10, padx=20, sticky="w")

#============OK Button============
NKWind.ok_btn = customtkinter.CTkButton(master=NKWind.frame_left, text="Ok", width=120)
NKWind.ok_btn.grid( row=11, column=1, pady=10, padx=20, sticky="e")




#                                              ========================== Right Frame ==========================

#============2x2 grid config============
NKWind.frame_right.grid_rowconfigure(0, weight=0)
NKWind.frame_right.grid_rowconfigure(1, weight=1)
NKWind.frame_right.grid_columnconfigure(1, weight=1)
NKWind.frame_right.grid_columnconfigure(0, weight=1)

#============ Selected and Preview Label ============

NKWind.frame_right.Selected_Lbl = customtkinter.CTkLabel(master=NKWind.frame_right, text="Selected Files",corner_radius=6, fg_color=("white", "gray38"))
NKWind.frame_right.Selected_Lbl.grid(row=0,column=0, padx=5, pady=5, sticky="nsew")

NKWind.frame_right.Preview_Lbl = customtkinter.CTkLabel(master=NKWind.frame_right, text="Preview",corner_radius=6, fg_color=("white", "gray38"))
NKWind.frame_right.Preview_Lbl.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

#============Scroll Bar For ListBoxes============

scroll_bar = Scrollbar(NKWind.frame_right, orient=VERTICAL)



#============ selected and preview listboxes ============

Preview_Files_LB = Listbox(master=NKWind.frame_right, bg="#2a2d2e",  yscrollcommand=scroll_bar.set)
Preview_Files_LB.grid(row=1,column=0, padx=5, pady=3, sticky="nsew",rowspan=2)

Selected_Files_LB = Listbox(master=NKWind.frame_right, bg="#2a2d2e", yscrollcommand=scroll_bar.set)
Selected_Files_LB.grid(row=1,column=1, padx=5, pady=3,sticky="nsew", rowspan=2)

#============ Scroll Bar Config ============
scroll_bar.config(command=Preview_Files_LB.yview)
scroll_bar.grid(row=1,column=3, padx=5, pady=3,sticky="ns")


#============Main Loop============
NKWind.mainloop()
