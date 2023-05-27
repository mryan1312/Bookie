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
    filetypes = ('Epub', '*.epub'),('PDF', '*.pdf'),('Text Files', '*.txt'),('All Files', '*.*')
    filename = fd.askopenfilename(title = 'Import', initialdir='/', filetypes=filetypes)
    file_name = re.search(r"/([a-zA-Z0-9-_# \(\),]*)\.([\w]*)", filename).group(1)  #There are easier ways, but I want to use regex :3
    file_extension = re.search(r"/([a-zA-Z0-9-_# \(\),]*)\.([\w]*)", filename).group(2)
    library = 'C:/Bookie/Library/'
    shutil.move(filename, library)
    library_data = [file_name, library+file_name+"."+file_extension]
    with open('C:/Bookie/library.csv', 'a') as datafile:
        writer = csv.writer(datafile)
        writer.writerow(library_data)
    if filename != '':
        showinfo(title = 'Import Complete', message=filename)

def data_directory():
    directory = 'Bookie'
    book_storage = 'Library'
    parent_dir = 'C:/'
    path = os.path.join(parent_dir, directory)
    lib_path = os.path.join(path, book_storage)
    if os.path.isdir(path) == False:
        os.mkdir(path)
    if os.path.isdir(lib_path) == False:
        os.mkdir(lib_path)
    data_file = "library.csv"
    file = os.path.join(path, data_file)
    if os.path.isfile(file) == False:
        with open(file, 'w') as library:
            pass

def btn_click():
    pass
    
#Main Window
data_directory()
m = tkinter.Tk()
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
with open("C:/Bookie/library.csv") as file:
    read = csv.reader(file, delimiter = ',')
    lib_dict = {}
    for row in read:
        lib_dict.append()
    buttons = lib_dict.keys()
    for btn in buttons:
        new_btn = Button(m, txt=btn, command=btn_click)
        new_btn.pack()
m.config(menu = menubar)
m.mainloop()

