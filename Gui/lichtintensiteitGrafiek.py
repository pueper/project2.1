import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Methode om de grafiek van de lichtintensiteit grafiek te weergeven
def showPagina():

    plt.style.use('fivethirtyeight')

    tijd = []               # een array waarin de tijden komen van de metingen
    # Een array waarin de waarden van de lichtintensiteit metingen moeten komen
    licht = []
    index = count()  # Een index maken die de tel bijhoudt

# Functie om een grafiek te genereren
    def genereerGrafiek(i):

        # Het volgende nummer in de array 'tijd' zetten
        tijd.append(next(index))
        # Omdat de verbinding met de arduino niet is gelukt, met random waardes om te laten zien dat de grafiek werkt
        licht.append(random.randint(3, 5))
        plt.cla()
        # De grafiek weergeven
        plt.plot(tijd, licht)

    # De functie om de genereiek te genereren wordt per seconde aangeroepen (Deze is te veranderen naar 60 sec = 60000)
    ani = FuncAnimation(plt.gcf(), genereerGrafiek, interval=1000)

    plt.tight_layout()
    plt.show()  # tot slot de grafiek weergeven
