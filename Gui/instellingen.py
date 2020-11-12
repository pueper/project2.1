import tkinter as tk

# variabele voor de minimale- en maximale uitrol stand.
maxUitrolInCm = str(160)
maxInrolInCm = str(0.5)


def showPagina():

    root = tk.Tk()

    # instellingen voor fullscreen
    root.overrideredirect(True)
    # instellingen voor fullscreen
    root.geometry(
        "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    # instellingen voor fullscreen
    root.focus_set()
    # instellingen voor fullscreen
    root.bind("<Escape>", lambda e: e.widget.quit())

    # de titel
    root.title("Overzicht lichtintensiteit")
    # tekstvak
    instellingenTekst = tk.Label(root, text="Overzicht Instellingen: \n\n\n De maximale inrolstand is: " + maxInrolInCm + " centimeter \n" +
                                 "De maximale uitrolstand is: " + maxUitrolInCm + " centimeter",
                                 font=40)

    # button makenom de pagina te sluiten
    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    instellingenTekst.pack()
    buttonExit.pack()

    # het plaatsen van de tekst en de knoppen
    instellingenTekst.place(x=800, y=200)
    buttonExit.place(x=1100, y=1000)

    root.mainloop()
