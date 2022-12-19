import os

prefix = input()
folder = r"C:\Users\Khung\Desktop\Python Lab"
filesRename = os.listdir(folder)  # List of Files
num_files = len(filesRename)
# Iterate
suf = 65 # Taking Suffix as 1
for file in os.listdir(folder):
    # Checking if the file is present in the list
    if file in filesRename:
        oldName = os.path.join(folder, file)
        n = os.path.splitext(file)[0]  # Path of the files excluding the Extension

        ext = os.path.splitext(file)[1]  # Extension of the file is stored in this variable

        b = prefix + " " +  str(chr(suf)) + ext  # New Name

        if(suf <90 or suf>96):
            suf += 1
        if(suf>=90):
            suf = 97
        # Numbering System

        newName = os.path.join(folder, b)

        # Renaming the file
        os.rename(oldName, newName)