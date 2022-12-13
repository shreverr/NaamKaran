import os
print(dir(os))
a = os.getcwd() # This is the method to know that in which directory you are currently working in
a = os.chdir(r"\Users\Khung\Desktop\Temp")
b = os.listdir(a) # List all files in the directory

path = r"C:\Users\Khung\Desktop\Temp\Fuck_Fuck"
x = os.path.splitext(path)[0]
print(x)