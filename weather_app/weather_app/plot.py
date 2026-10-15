from matplotlib.figure import (Figure)
from menu import *

# ----------------------------------------------------------------------
# Plot Matplotlib
# ----------------------------------------------------------------------

def create_plot(dates, temperatures_min, temperatures_max):
    """Crée et retourne une Figure Matplotlib avec les courbes de températures min et max sur les dates fournies."""
    figure = Figure(figsize = (3.5,3))
    axes = figure.add_subplot(111)

    axes.plot(dates,temperatures_min,label="Température ninimale (°C)",color="blue",marker="o")
    axes.plot(dates, temperatures_max, label="Température maximale (°C)", color="red", marker="o")

    axes.set_title("Températures (°C)")
    axes.legend()
    axes.grid(True)

    axes.set_xticks(range(len(dates)))
    axes.set_xticklabels(dates, rotation=45)

    figure.tight_layout()

    return figure


def draw_forecast(window, canvas):
    if canvas is not None:
        canvas.get_tk_widget().destroy()
    dates, t_min, t_max = get_forecast()
    figure = create_plot(dates, t_min, t_max)
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    return canvas
