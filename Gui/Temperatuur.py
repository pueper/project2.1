import tkinter as tk


def showPagina():
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry(
        "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()
    root.bind("<Escape>", lambda e: e.widget.quit())

    temparatuurPaginaTekst = tk.Label(root, text="Overzicht temperatuursensor",
                                      font=40)
    root.title("Overzicht temperatuursensor")
    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    temparatuurPaginaTekst.pack()
    buttonExit.pack()

    temparatuurPaginaTekst.place(x=850, y=200)
    buttonExit.place(x=1100, y=1000)
    root.mainloop()
