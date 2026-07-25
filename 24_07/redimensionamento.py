#redimensionamento da janela
import tkinter as tk

root = tk.Tk()
root.title("Senai, Logica de programação")
root.geometry("400x300")

root.resizable(True, True)


root.minsize(200, 200)
root.maxsize(600, 600)
root.attributes("-alpha", 0.5)
root.mainloop()