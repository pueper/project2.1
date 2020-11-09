import tkinter as tk
from tkinter import *

def showPagina():

    root = tk.Tk()

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

    #het weergeven van de grafiek op de pagina
    grafiek = Canvas(root, width=300, height=300)
    grafiek.pack()
    img = PhotoImage(file="licht.png")
    grafiek.create_image(20, 20, image=img)

    # De titel van de pagina
    root.title("Overzicht lichtintensiteit")

    # Button om terug te gaan naar de hoofdpagina
    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    buttonExit.pack()
    lichtintensiteitPaginaTekst.pack()

    # De tekst en button een positie geven op de pagina
    lichtintensiteitPaginaTekst.place(x=850, y=200)
    buttonExit.place(x=1100, y=1000)

    root.mainloop()
