import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import re
import csv
import sys
import shutil
import os

def library_import():
    file = fd.askopenfilename(title = 'Import', initialdir='/', filetypes=[("All Files", "*.*")])
    #guard condition so the program doesnt fail
    if file == '':
        showinfo(title = 'Import Error', message="file no selected")
    #There are easier ways, but I want to use regex :3
    #sorry to kill your ways :(
    filename = file.split("/")[-1]
    file_name= filename.split(".")[0]
    destination_folder = './Library/'
    destination = os.path.join(destination_folder , filename) 
    #we create the folder if it doesnt exsist
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    #use copy as to not move the original file rather copy it
    shutil.copy(file, destination)
    library_data = [file_name, destination]
    with open( './library.csv', 'a') as datafile:
        writer = csv.writer(datafile)
        writer.writerow(library_data)
    showinfo(title = 'Import Complete', message=filename)
    


def list_select(event):
    selected_indices = title_listbox.curselection()
    if not selected_indices == "":
        try:
            msg = title_listbox.get(selected_indices)
            showinfo(title = 'Selection', message = msg)
        except:
            pass

#Main Window
m = tkinter.Tk()
title_frame = Frame(m)
title_frame.pack(side = LEFT, expand = True, fill = BOTH)
v = Scrollbar(title_frame)
v.pack(side = RIGHT, expand = True, fill = BOTH)
m.title('Bookie')

#Menu
menubar = Menu(m)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = file)
file.add_command(label = 'Import', command = library_import)
file.add_command(label = 'Exit', command = None)
tools = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Tools', menu = tools)
about = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='About', menu = about)
about.add_command(label ='About', command = None)
about.add_command(label ='Help', command = None)

#Display Library Files
if not os.path.isfile('./library.csv'):
    with open('./library.csv', 'w') as file:
        file.close()
with open("./library.csv") as file:
    read = csv.reader(file, delimiter = ',')
    lib_dict = []
    for row in read:
        if row != []:
            lib_dict.append([row[0]])
title_keys = tkinter.Variable(value = lib_dict)
title_listbox = tkinter.Listbox(title_frame, listvariable = title_keys, selectmode = tkinter.EXTENDED)
title_listbox.pack(expand = True, fill = tkinter.BOTH)

m.config(menu = menubar)
title_listbox.bind('<<ListboxSelect>>', list_select)
m.mainloop()

