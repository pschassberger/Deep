# writing a newer vertsion of the game to play with the NN better

import tkinter as tk
from random import randint
from PIL import Image, ImageTk
import random

def window():
    # title
    window = tk.Tk()
    window.title("nn-Snake")
    window.mainloop()
    window.resizable(False,False)

    #Canvas
    canvas = Canvas(window, width=1000, height=1000)
    canvas.pack()

    canvas.mainloop()


window()