import tkinter as tk
import Temperatuur as temperatuur
import lichtintensiteit as lichtintensiteit
import instellingen as instellingen


class Gui():
    def __init__(self):
        self.isUitgerold = False
        self.root = tk.Tk()

        # instellingen voor fullscreen
        self.root.overrideredirect(True)
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))     # instellingen voor fullscreen
        # instellingen voor fullscreen
        self.root.focus_set()
        # instellingen voor fullscreen
        self.root.bind("<Escape>", lambda e: e.widget.quit())

        self.label = tk.Label(
            self.root, text="Welkom op de Zonnescherm GUI", font=800)
        buttonNaarTemperatuur = tk.Button(
            self.root, text="Naar temperatuur overzicht", command=self.naarTemperatuur)

        buttonNaarLichtintensiteit = tk.Button(
            self.root, text="Naar lichtintensiteit overzicht", command=self.naarLichtintensiteit)

        buttonNaarInstellingen = tk.Button(
            self.root, text="Naar instellingen", command=self.naarInstellingen)

        buttonExit = tk.Button(
            self.root, text="Afsluiten", command=self.root.destroy)

        self.label2 = tk.Label(
            self.root, text="Het Zonnescherm handmatig bedienen")

        buttonRolZonneSchermIn = tk.Button(
            self.root, text="Rol het zonnescherm in", command=self.rolZonneSchermIn)

        buttonRolZonneSchermUit = tk.Button(
            self.root, text="Rol het zonnescherm uit", command=self.rolZonneSchermUit)

        self.label.place(x=850, y=400)
        self.label2.place(x=870, y=650)

        buttonNaarTemperatuur.pack()
        buttonNaarLichtintensiteit.pack()
        buttonNaarInstellingen.pack()
        buttonExit.pack()
        buttonRolZonneSchermIn.pack()
        buttonRolZonneSchermUit.pack()

        buttonNaarTemperatuur.place(x=600, y=1000)
        buttonNaarLichtintensiteit.place(x=780, y=1000)
        buttonNaarInstellingen.place(x=970, y=1000)
        buttonExit.place(x=1100, y=1000)
        buttonRolZonneSchermIn.place(x=900, y=700)
        buttonRolZonneSchermUit.place(x=900, y=730)

        self.root.mainloop()

    # Naar de temperatuur pagina gaan
    def naarTemperatuur(self):
        temperatuur.showPagina()

    # Naar de lichtintensiteit pagina gaan
    def naarLichtintensiteit(self):
        lichtintensiteit.showPagina()

    # Naar de instellingen pagina gaan
    def naarInstellingen(self):
        instellingen.showPagina()

    def rolZonneSchermIn(self):
        pass
        # Hier de code om het zonnescherm in te rollen
        # Als dit is gelukt self.isUitgerold op False zetten

    def rolZonneSchermUit(self):
        pass

        # Hier de code om het zonnescherm uit te rollen
        # als dit is gelukt self.isUitgerold op True zetten


gui = Gui()
