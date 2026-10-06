# Projet appli météo

import tkinter as tk

from constants import *
from menu import *

# Window et Canvas Tkinter
# Ces variables globales permettent d'éviter que le garbage collector ne les efface
window = None
canvas = None

# ----------------------------------------------------------------------
# Programme principal
# ----------------------------------------------------------------------

def main():
    global window, canvas
    global image_background
    window = tk.Tk()

    canvas = tk.Canvas(window, width=400, height= 500)
    canvas.pack()

    load_background(canvas)
    draw_welcome_screen(window, canvas)
    window.mainloop()

if __name__ == "__main__":
    main()
