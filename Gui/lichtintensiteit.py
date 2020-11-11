import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import Verbinding as verbinding


lichtintensiteit = verbinding.lichtintensiteit
tijd = verbinding.tijd
gemiddelde_lichtintensiteit = verbinding.gemiddelde_lichtintensiteit


def showPagina():

    root = tk.Tk()

    data = {"Tijd": tijd, "Lichtintensiteit": lichtintensiteit}
    df = DataFrame(data, columns=['Tijd', 'Lichtintensiteit'])
    figure = plt.Figure(figsize=(12, 12), dpi=50)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().place(x=600, y=300)
    df = df[['Tijd', 'Lichtintensiteit']].groupby('Tijd').sum()
    df.plot(kind='line', legend=True, ax=ax)
    ax.set_title("De gemeten lichtintensiteit per 60 seconden")

    # instellingen voor full screen
    root.overrideredirect(True)
    # instellingen voor full screen
    root.geometry(
        "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    # instellingen voor full screen
    root.focus_set()
    # instellingen voor full screen
    root.bind("<Escape>", lambda e: e.widget.quit())

    # De tekst die op de pagina wordt weergeven
    lichtintensiteitPaginaTekst = tk.Label(root, text="Overzicht lichtintensiteit",
                                           font=40)

    # De titel van de pagina
    root.title("Overzicht lichtintensiteit")

    # Button om terug te gaan naar de hoofdpagina
    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    gemiddeldeLichtintensiteitTekst = tk.Label(
        root, text="Gemiddelde Lichtintensiteit: " + gemiddelde_lichtintensiteit, font=40)

    buttonExit.pack()
    lichtintensiteitPaginaTekst.pack()

    # De tekst en button een positie geven op de pagina
    lichtintensiteitPaginaTekst.place(x=850, y=200)
    buttonExit.place(x=1100, y=1000)
    gemiddeldeLichtintensiteitTekst.place(x=1300, y=445)

    root.mainloop()
