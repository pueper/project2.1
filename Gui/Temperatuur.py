import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import Verbinding as verbinding

tijd = verbinding.tijd
temperatuur = verbinding.temperatuur
gemiddelde_temperatuur = verbinding.gemiddelde_temperatuur


def showPagina():

    root = tk.Tk()

    data = {"Tijd": tijd, "Temperatuur": temperatuur}
    df = DataFrame(data, columns=['Tijd', 'Temperatuur'])
    figure = plt.Figure(figsize=(12, 12), dpi=50)
    ax = figure.add_subplot(111)
    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().place(x=600, y=250)
    df = df[['Tijd', 'Temperatuur']].groupby('Tijd').sum()
    df.plot(kind='line', legend=True, ax=ax)
    ax.set_title("De gemeten temperatuur per 60 seconden")

    # Instellingen voor full screen
    root.overrideredirect(True)
    # Instellingen voor full screen
    root.geometry(
        "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    # Instellingen voor full screen
    root.focus_set()
    # Instellingen voor full screen
    root.bind("<Escape>", lambda e: e.widget.quit())

    # De tekst die op de pagina wordt weergeven
    temparatuurPaginaTekst = tk.Label(root, text="Overzicht temperatuursensor",
                                      font=40)
    gemiddeldeTemperatuurTekst = tk.Label(
        root, text="Gemiddelde temperatuur: " + gemiddelde_temperatuur + " Graden Celcius", font=40)

    # De titel van de pagina
    root.title("Overzicht temperatuursensor")
    # De knop om terug te gaan naar de hoofdpagina
    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    temparatuurPaginaTekst.pack()
    buttonExit.pack()

    # De knoppen en de tekst een positie geven op de pagina
    temparatuurPaginaTekst.place(x=850, y=200)
    gemiddeldeTemperatuurTekst.place(x=1300, y=445)
    buttonExit.place(x=1100, y=1000)
    root.mainloop()

    # Hier moet nog een grafiek komen, je moet zelf maar even kijken wat handig is qua hoe je de gelezen data op moet slaan.
    # Vervolgens kan je uit deze data een grafiek maken (Dit moet wel om de zoveel seconde gebeuren)
