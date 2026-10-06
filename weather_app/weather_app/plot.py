from matplotlib.figure import Figure

# ----------------------------------------------------------------------
# Plot Matplotlib
# ----------------------------------------------------------------------

def create_plot(dates, temperatures_min, temperatures_max):
    """Crée et retourne une Figure Matplotlib avec les courbes de températures min et max sur les dates fournies."""
    figure = Figure(figsize = (3.8, 3.2))
    axes = figure.add_subplot(111)
    axes.plot(dates,temperatures_min,label="Température ninimale (°C)",color="red",marker="o")
    axes.legend()
    axes.grid(True)
    axes.set_xticks(range(len(dates)))
    axes.set_xticklabels([d[5:] for d in dates], rotation = 45)
    figure.tight_layout()
    return figure
def draw_forecast(window,canvas):
    
