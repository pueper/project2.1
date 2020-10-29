import tkinter as tk
import TemperatuurGrafiek as temperatuur
import lichtintensiteit as lichtintensiteit
import instellingen as instellingen


class Gui():
    def __init__(self):
        self.isUitgerold = False
        self.root = tk.Tk()

        self.label = tk.Label(
            self.root, text="Welkom op de Zonnescherm GUI", width=175, height=60).pack()
        buttonNaarTemperatuur = tk.Button(
            self.root, text="Naar temperatuur overzicht", command=self.naarTemperatuur).pack()
        buttonNaarLichtintensiteit = tk.Button(
            self.root, text="Naar lichtintensiteit overzicht", command=self.naarLichtintensiteit).pack()
        buttonNaarInstellingen = tk.Button(
            self.root, text="Naar instellingen", command=self.naarInstellingen).pack()
        self.root.mainloop()

    def naarTemperatuur(self):
        temperatuur.showPagina()

    def naarLichtintensiteit(self):
        lichtintensiteit.showPagina()

    def naarInstellingen(self):
        instellingen.showPagina()

    def rolIn(self):
        self.isUitgerold = False

    def rolUit(self):
        self.isUitgerold = True


gui = Gui()
