import tkinter as tk

# variabele voor de minimale- en maximale uitrol stand, deze kan je zelf nog aanpassen
maxUitrolInCm = str(100)
maxInrolInCm = str(20)


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

    # Er moeten nog een functie komen om de minimale/maximale uitrolstand te veranderen.
    # Dit kan d.m.v. van een tekstvak en een button die verwijst naar een functie
    # In deze functie kan je de variabele (maxInrolInCm en MaxUitrolInCm) aanpasssen, naar de waarde die uit het tekstvak wordt gelezen
    # Vervolgens kan je deze waarde naar het bordje sturen
