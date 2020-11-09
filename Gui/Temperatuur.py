import tkinter as tk
from tkinter import *

def showPagina():
    root = tk.Tk()

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

    #grafiek weergeven op de pagina
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()
    img = PhotoImage(file="temp.png")
    canvas.create_image(20, 20, anchor=NW, image=img)

    # De titel van de pagina
    root.title("Overzicht temperatuursensor")
    # De knop om terug te gaan naar de hoofdpagina
    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    temparatuurPaginaTekst.pack()
    buttonExit.pack()

    # De knoppen en de tekst een positie geven op de pagina
    temparatuurPaginaTekst.place(x=850, y=200)
    buttonExit.place(x=1100, y=1000)
    root.mainloop()

    # Hier moet nog een grafiek komen, je moet zelf maar even kijken wat handig is qua hoe je de gelezen data op moet slaan.
    # Vervolgens kan je uit deze data een grafiek maken (Dit moet wel om de zoveel seconde gebeuren)
