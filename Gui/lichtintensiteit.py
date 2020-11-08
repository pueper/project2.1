import tkinter as tk


def showPagina():

    root = tk.Tk()

    root.overrideredirect(True)
    root.geometry(
        "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()
    root.bind("<Escape>", lambda e: e.widget.quit())

    lichtintensiteitPaginaTekst = tk.Label(root, text="Overzicht lichtintensiteit",
                                           font=40)
    root.title("Overzicht lichtintensiteit")

    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    buttonExit.pack()
    lichtintensiteitPaginaTekst.pack()

    lichtintensiteitPaginaTekst.place(x=850, y=200)
    buttonExit.place(x=1100, y=1000)

    root.mainloop()
