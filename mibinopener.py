from lib2to3.pgen2.token import STRING
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from tkinter import filedialog
import os
import zipfile

def file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Zepp Firmware', '*.bin'), ('Archive', '*.zip')])
    if file:
      etrTitle.delete(0,"end")
      filepath = os.path.abspath(file.name)
      etrTitle.insert(STRING, str(filepath))

def folder():
    folder = filedialog.askdirectory(initialdir="/", title="Select file")
    if folder:
      etrExtract.delete(0,"end")
      etrExtract.insert(STRING, str(folder))

def renameBin():
      thisFile = etrTitle.get()
      base = os.path.splitext(thisFile)[0]
      os.rename(thisFile, base + ".zip")

def unpack():
      firmware = zipfile.ZipFile(etrTitle.get(), 'r')
      firmware.extractall(etrExtract.get())

root = ttk.Window(themename="darkly", resizable=(False, False))
root.title("MiBinOpener")
root.place_window_center()

labTitle = ttk.Label(text="Choose .bin file")
etrTitle = ttk.Entry(width=50)
labExtract = ttk.Label(text="Choose folder to extract")
etrExtract = ttk.Entry(width=50)
btnFile = ttk.Button(command=file, text="Open", bootstyle="secondary")
btnFolder = ttk.Button(command=folder, text="Choose", bootstyle="secondary")
btnRename = ttk.Button(command=renameBin, text=".bin > .zip", bootstyle="secondary")
btnStart = ttk.Button(command=unpack, text="Start")
ToolTip(btnRename, text="If you change the file type, you need to select the file again", bootstyle=(DANGER, INVERSE))

labTitle.grid(row=0, column=0, sticky=W, padx=10, pady=10)
etrTitle.grid(row=1, column=0, columnspan=3, sticky=W, padx=10)
labExtract.grid(row=2, column=0, sticky=W, padx=10, pady=10)
etrExtract.grid(row=3, column=0, columnspan=3, sticky=W, padx=10)
btnFile.grid(row=1, column=4, sticky=W)
btnFolder.grid(row=3, column=4, sticky=W)
btnRename.grid(row=1, column=5, sticky=W, padx=10)
btnStart.grid(row=4, column=0, sticky=W, padx=10, pady=10)

root.mainloop()