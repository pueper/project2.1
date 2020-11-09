import tkinter as tk
import Temperatuur as temperatuur
import lichtintensiteit as lichtintensiteit
import instellingen as instellingen
#from serial import lengte_zonnescherm

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

        # tekstvak
        self.label = tk.Label(
            self.root, text="Welkom op de Zonnescherm GUI", font=800)

        # knop om naar het temperatuur overzicht te gaan (temperatuur.py)
        buttonNaarTemperatuur = tk.Button(
            self.root, text="Naar temperatuur overzicht", command=self.naarTemperatuur)

        # knop om naar het lichtintensiteit overzicht te gaan (lichtintensiteit.py)
        buttonNaarLichtintensiteit = tk.Button(
            self.root, text="Naar lichtintensiteit overzicht", command=self.naarLichtintensiteit)

        # knop om naar instellingen overzicht te gaan (instellingen.py)
        buttonNaarInstellingen = tk.Button(
            self.root, text="Naar instellingen", command=self.naarInstellingen)

        # knop om de gehele gui af te sluiten
        buttonExit = tk.Button(
            self.root, text="Afsluiten", command=self.root.destroy)

        # 2e tekstvak
        self.label2 = tk.Label(
            self.root, text="Het Zonnescherm handmatig bedienen")

        # knop om het zonnescherm in te rollen (gaat naar de functie rolZonneSchermIn, hier nog even de code toevoegen om dit te realiseren)
        buttonRolZonneSchermIn = tk.Button(
            self.root, text="Rol het zonnescherm in", command=self.rolZonneSchermIn)

        # knop om het zonnescherm uit te rollen (gaat naar de functie rolZonneSchermUit, hier nog even de code toevoegen om dit te realiseren)
        buttonRolZonneSchermUit = tk.Button(
            self.root, text="Rol het zonnescherm uit", command=self.rolZonneSchermUit)

        # De teksten een positie geven op de pagina
        self.label.place(x=850, y=400)
        self.label2.place(x=870, y=650)

        buttonNaarTemperatuur.pack()
        buttonNaarLichtintensiteit.pack()
        buttonNaarInstellingen.pack()
        buttonExit.pack()
        buttonRolZonneSchermIn.pack()
        buttonRolZonneSchermUit.pack()

        # de knoppen een positie geven op de pagina
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
        #lengte = lengte_zonnescherm()
        #if (lengte > 0,05):
        #   lengte = 0,05
        #   self.isUitgerold = False
        #else:
        #   print("Het zonnescherm is al compleet ingerold.")

    def rolZonneSchermUit(self):
        pass
        #lengte = lengte_zonnescherm()
        #if (lengte < 1,60):
        #   lengte = 1,60
        #   self.isUitgerold = True
        #else:
        #   print("Het zonnescherm kan niet verder worden uitgerold.")


gui = Gui()


# Hier moet nog een functie komen om het zonnescherm handmatig in- of uit te rollen.
# Dit kan misschien met de boolean isUitgerold, dat je deze wijzigt en dat de arduino dit leest en vervolgens hier iets mee doet
# Ik heb al knoppen gemaakt die je naar de bijbehorende functie stuurt, in deze functie kan je dan deze boolean aanpassen, en hier
# Kan de arduino dan op reageren.
