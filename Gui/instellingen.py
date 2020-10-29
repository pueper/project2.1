import tkinter as tk

maxUitrolInCm = str(100)
maxInrolInCm = str(20)


def showPagina():

    window = tk.Tk()
    window.title("Overzicht lichtintensiteit")
    tk.Label(window, text="Overzicht Instellingen\nHieronder een overzicht van de instellingen: \n\n\n De maximale inrolstand is: " + maxInrolInCm + " centimeter \n" +
             "De maximale uitrolstand is: " + maxUitrolInCm + " centimeter",
             fg="blue", width=175, height=60).pack()

    wijzigenMaximaleUitrol = tk.Text(window, height=1, width=10).pack()
    window.mainloop()


def wijzigingMaxUitrolOpslaan(arg):
    maxIntrolInCm = arg


def wijzigingMaxInrolOpslaan(arg):
    maxUitrolInCm = arg
