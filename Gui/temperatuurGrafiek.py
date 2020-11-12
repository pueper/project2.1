import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Methode die vanuit de GUI wordt aangeroepen, om de grafiek van de temperatuur te weergeven
def showPagina():
    plt.style.use('fivethirtyeight')

    tijd = []  # een array met de tijden waarop gemeten wordt

    # een array waarin de waarden die worden gemeten van de temperatuursensor worden opgeslagen
    temperaturen = []
    index = count()

    # Methode om de grafiek te genereren
    def genereerGrafiek(i):
        tijd.append(next(index))
        temperaturen.append(random.randint(3, 5))
        plt.cla()
        plt.plot(tijd, temperaturen)

    # De functie om de genereiek te genereren wordt per seconde aangeroepen (deze is te veranderen naar 60 sec = 60000)
    ani = FuncAnimation(plt.gcf(), genereerGrafiek, interval=1000)

    plt.tight_layout()
    plt.show()  # Tot slot de grafiek weergeven
