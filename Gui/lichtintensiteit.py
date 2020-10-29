import tkinter as tk


def showPagina():

    window = tk.Tk()
    tk.Label(window, text="Overzicht temperatuursensor",
             fg="blue", width=175, height=60).pack()
    window.title("Overzicht lichtintensiteit")
    window.mainloop()
