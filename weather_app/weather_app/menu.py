import tkinter as tk
from PIL import Image, ImageTk
from PIL.ImageChops import offset
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

def change_city(new_city, window, canvas):
    """Appelée quand l'utilisateur choisit une ville dans le menu déroulant."""
    global city
    city = new_city
    draw_welcome_screen(window, canvas)


def draw_welcome_screen(window, canvas):
    """Écran 1 : Icône de la météo, température actuelle, températures min et max du jour."""
    global weather_icon

    erase_screen(canvas)
    temperature, code, t_min, t_max = get_current_weather(city)

    canvas.create_text(200, 50, text=f"{city}", font=("Arial", 24, "bold"), fill="white", tags="ecran")

    # Menu déroulant pour choisir la ville
    city_var = tk.StringVar(value=city)
    city_menu = tk.OptionMenu(
        window,
        city_var,
        *CITIES.keys(),
        command=lambda choice: change_city(choice, window, canvas)
    )
    city_menu.config(font=("Arial", 18, "bold"))
    canvas.create_window(200, 50, window=city_menu, tags="ecran")


    # global weather_icon
    img = Image.open("assets/icons/sunny.png")
    img = img.resize((80, 80))
    weather_icon = ImageTk.PhotoImage(img)
    canvas.create_image(200, 160, image=weather_icon, tags="ecran")

    canvas.create_text(200, 280, text=f" {temperature}°C", fill="white", font=("Arial", 24, "bold"), tags="ecran")
    canvas.create_text(200, 350, text=f"Min : {t_min}°C                Max : {t_max}°C", fill="white", tags="ecran")

    button = tk.Button(window, text="Prévisions 7 jours", command=lambda:draw_forecast(window, canvas))
    canvas.create_window(200, 400, window=button, tags="ecran")


def draw_forecast(window, canvas,offset=0):
    erase_screen(canvas)
    MIN_OFFSET = -84
    MAX_OFFSET = 9

    canvas.create_text(
        200,
        40,
        text=f"Prévisions sur 7 jours - {city}",
        font=("Arial", 18, "bold"),
        fill="white",
        tags="ecran"
    )

    start_day = date.today() + timedelta(days=offset)

    dates, t_mins, t_maxs = get_forecast(
        city,
        start_day
    )

    canvas.create_text(
        200,
        75,
        text=f"Du {dates[0]} au {dates[-1]}",
        font=("Arial", 10, "bold"),
        fill="white",
        tags="ecran"
    )

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

    button_left = tk.Button(
        window,
        text="◀",
        width=3,
        state=tk.NORMAL if offset > 0 else tk.DISABLED,
        command=lambda: draw_forecast(window, canvas, offset - 7)
    )

    button_accueil = tk.Button(
        window,
        text="Accueil",
        command=lambda: draw_welcome_screen(window, canvas)
    )

    button_right = tk.Button(
        window,
        text="▶",
        width=3,
        state=tk.NORMAL if offset + 7 <= 9 else tk.DISABLED,
        command=lambda: draw_forecast(window, canvas, offset + 7)
    )

    canvas.create_window(
        120,
        460,
        window=button_left,
        tags="ecran"
    )

    canvas.create_window(
        200,
        460,
        window=button_accueil,
        tags="ecran"
    )

    canvas.create_window(
        280,
        460,
        window=button_right,
        tags="ecran"
    )
