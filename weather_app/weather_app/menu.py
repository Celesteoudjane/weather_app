import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import date

from constants import *
from weather import *
from weather_queries import *
from plot import *

# ----------------------------------------------------------------------
# Variables globales
# ----------------------------------------------------------------------
# Ville actuelle
city = "Paris"
# city = "Bordeaux"

# ImageTk : ces variables globales permettent d'éviter que le garbage collector ne les efface
image_background = None
weather_icon = None

# ----------------------------------------------------------------------
# Canvas
# ----------------------------------------------------------------------

def load_background(canvas):
    """Charge "assets/blue_sky.jpg", la redimensionne et la place sur le canvas."""
    global image_background

    image = Image.open("assets/blue_sky.jpg").convert("RGBA")
    image = image.resize((WIDTH, HEIGHT))
    image_background = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=image_background, anchor="nw")


def erase_screen(canvas):
    """Supprime tout ce qui a le tag 'ecran'."""
    canvas.delete("ecran")


# ----------------------------------------------------------------------
# Ecrans
# ----------------------------------------------------------------------

def draw_welcome_screen(window, canvas):
    """Écran 1 : Icône de la météo, température actuelle, températures min et max du jour."""
    global weather_icon

    erase_screen(canvas)
    # temperature, code, t_min, t_max = 0, 0, 0, 0
    temperature = 19.7
    code = 0
    t_min, t_max = 18.0, 27.4

    canvas.create_text(200, 50, text=f"{city}", font=("Arial", 24, "bold"), fill="white", tags="ecran")

    global weather_icon
    img = Image.open("assets/icons/sunny.png")
    img = img.resize((80, 80))
    weather_icon = ImageTk.PhotoImage(img)
    canvas.create_image(200, 160, image=weather_icon, tags="ecran")

    canvas.create_text(200, 280, text=f" {temperature}°C", fill="white", font=("Arial", 24, "bold"), tags="ecran")
    canvas.create_text(200, 350, text=f"Min : {t_min}°C                Max : {t_max}°C", fill="white", tags="ecran")

    button = tk.Button(window, text="Prévisions 7 jours", command=lambda:draw_forecast(window, canvas))
    canvas.create_window(200, 400, window=button, tags="ecran")


def draw_forecast(window, canvas):
    erase_screen(canvas)

    canvas.create_text(
        200,
        40,
        text=f"Prévisions sur 7 jours - {city}",
        font=("Arial", 18, "bold"),
        fill="white",
        tags="ecran"
    )

    canvas.create_text(
        200,
        70,
        text="Du 2026-10-05 au 2026-10-11",
        font=("Arial", 14),
        fill="white",
        tags="ecran"
    )

    dates = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]

    t_mins = [18, 17, 16, 15, 17, 18, 19]
    t_maxs = [27, 26, 25, 24, 26, 28, 29]

    figure = create_plot(dates, t_mins, t_maxs)

    graph = FigureCanvasTkAgg(
        figure,
        master=window
    )

    graph.draw()

    canvas.create_window(
        200,      # center of 400 px canvas
        260,
        window=graph.get_tk_widget(),
        tags="ecran"
    )

    button = tk.Button(
        window,
        text="Accueil",
        command=lambda: draw_welcome_screen(window, canvas)
    )

    canvas.create_window(
        200,
        460,
        window=button,
        tags="ecran"
    )
