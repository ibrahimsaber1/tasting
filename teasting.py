import os, shutil
path = r"F:/lol/"
file_name = os.listdir(path)
['New Microsoft Word Document.docx',
 'NewYork1.jpg',
 'NewYork2.jpg',
 'NewYork3.jpg',
 'PLAN1.txt',
 'PLAN2.txt']
folder_names = ['txt files', 'images file', 'docx files']

for loop in range (0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
F:/lol/txt files
F:/lol/images file
F:/lol/docx files
import os

path = "F:/lol/"  # Replace this with the desired path

folder_names = ['txt files', 'images file', 'docx files']

for loop in range(0, 3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
F:/lol/txt files
os.makerids(path + dd)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[34], line 1
----> 1 os.makerids(path + dd)

AttributeError: module 'os' has no attribute 'makerids'
import os

path = "F:/lol/"  # Replace this with the desired path
dd = "tt.txt"  # Replace this with the desired directory name

os.makedirs(path + dd)
path = "F:/lol/"  # Replace this with the desired path
dd = "tt.txt"  # Replace this with the desired directory name

os.makedirs(path + dd)
file_name = os.listdir(path)
for file in file_name:
    if ".txt" in file and not os.path.exists(path + "txt files/" + file):
        shutil.move(path + file, path + "txt files/" + file)
import os
import shutil

path = "F:/lol/"  

file_names = os.listdir(path)

for file in file_names:
    if file.endswith(".txt") and not os.path.exists(path + "txt files/" + file):
        if not os.path.exists(path + "txt files"):
            os.makedirs(path + "txt files")
        shutil.move(path + file, path + "txt files/" + file)
import os
import shutil

path = "F:/lol/"   

file_names = os.listdir(path)

for file in file_names:
    if file.endswith(".jpg") and not os.path.exists(path + "images/" + file):
        if not os.path.exists(path + "images"):
            os.makedirs(path + "images")
        shutil.move(path + file, path + "images/" + file)
import os
import shutil

path = 'F:/lol/'  

file_names = os.listdir(path)

for file in file_names:
    if file.endswith(".docx") and not os.path.exists(path + "docx files/" + file):
        if not os.path.exists(path + "docx files"):
            os.makedirs(path + "docx files")
        shutil.move(path + file, path + "docx files/" + file)
