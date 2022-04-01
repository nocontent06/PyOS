#########################################################
# All necesscary import's for the OS

import code
import sys
import os
import platform
import time
import psutil
import cpuinfo
import socket
from tqdm import tqdm
##########################################################
# Import's for Tkinter

from tkinter import * 
import tkinter as tk, threading
try:
    from tkvideo import tkvideo
except:
    os.system("pip install tkvideo")

import imageio
from PIL import Image, ImageTk
#from bvPlayer import bvPlayer

##########################################################
# Some Variables before Tkinter
sys_ver = "1.3.1"
acc_c_ver = "0.1.1 beta"
##########################################################
root = Tk()
root.geometry("1280x720")
root.title("PyOS v" + sys_ver)
##########################################################
# Labels creating here:
my_label = Label(root)
my_label_2 = Label(root)

my_label.pack()
my_label_2.pack()
##########################################################

player = tkvideo("./resources/pyosboot.mov", my_label, loop = 0, size = (1280,720))
player.play()

#Button(my_label, text="Skip -->", command=my_label.deletecommand)
my_label.after(10000, my_label.destroy)


#bvPlayer("./resources/pyosboot.mov", dim=(1280,720))

Button(root, text="About my PC").pack(side=BOTTOM, expand=YES)


"""
if __name__ == "__main__":

    root = tk.Tk()
    root.geometry("1280x720")
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label))
    thread.daemon = 1
    thread.start()
    #tk.Label(root, text='Bottom left').grid(row=2, column=0, sticky='w')

    root.mainloop()
"""





















root.mainloop()