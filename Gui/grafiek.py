import matplotlib.pyplot as plt
#numpy is voor als we iets moeten berekenen tijdens het maken van
#de grafiek
#import numpy as np
#from serial import temperatuur_data, licht_data

#voor grafiek lichtsensitiviteit
def lichtsensitiviteit_plot():
       #hier laden we de data van de licht sensor in
       #c = licht data
       fig, ax = plt.subplots()
       #dan verwerken we hier variabele c in de plot
       ax.plot([1,2])       #1e nummer is voor beginwaarde,
                            # 2e nummer is stapgrootte

       #informatie aaan de assen rond de grafiek zetten
       ax.set(xlabel='tijd', ylabel='hoeveelheid licht',
              title='grafiek voor lichtsensitiveit')
       ax.grid() #voor de raster print op de achtergrond

       #sla op als afbeelding, laat afbeelding zien
       fig.savefig("licht.png") #sla op als file
       plt.show()           #laat zien bij runnen programma

#voor grafiek temperatuur
def temperatuur_plot():
       #hier laden we de data van de temp sensor in
       #b = temperatuur data
       fig, ax = plt.subplots()
       #dan verwerken we variabele b in de plot
       ax.plot([1, 5])      #1e nummer is voor beginwaarde,
                            # 2e nummer is stapgrootte

       #info aan de assen van de grafiek zetten
       ax.set(xlabel='tijd', ylabel='temperatuur',
              title='grafiek voor temperatuur')
       ax.grid()

       #afbeelding opslaan en grafiek laten zien
       fig.savefig("temp.png") #sla op als file
       plt.show()           #laat zien bij runnen programma

#runnen van de functies
lichtsensitiviteit_plot()
temperatuur_plot()