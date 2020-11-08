import tkinter as tk


def showPagina():

    root = tk.Tk()

    root.overrideredirect(True)
    root.geometry(
        "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()
    root.bind("<Escape>", lambda e: e.widget.quit())

    tk.Label(root, text="Overzicht temperatuursensor",
             fg="blue", width=175, height=60).pack()
    root.title("Overzicht temperatuursensor")

    buttonExit = tk.Button(
        root, text="Terug", command=root.destroy)

    buttonExit.pack()
    root.mainloop()
