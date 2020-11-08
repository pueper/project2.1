import tkinter as tk

maxUitrolInCm = str(100)                # deze waarde kan je zelf nog aanpassen
maxInrolInCm = str(20)


def showPagina():

    root = tk.Tk()

    # instellingen voor fullscreen
    root.overrideredirect(True)
    root.geometry(
        "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))     # instellingen voor fullscreen
    # instellingen voor fullscreen
    root.focus_set()
    # instellingen voor fullscreen
    root.bind("<Escape>", lambda e: e.widget.quit())

    root.title("Overzicht lichtintensiteit")
    instellingenTekst = tk.Label(root, text="Overzicht Instellingen: \n\n\n De maximale inrolstand is: " + maxInrolInCm + " centimeter \n" +
                                 "De maximale uitrolstand is: " + maxUitrolInCm + " centimeter",
                                 font=40)

    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    instellingenTekst.pack()
    buttonExit.pack()

    instellingenTekst.place(x=800, y=200)
    buttonExit.place(x=1100, y=1000)

    root.mainloop()
