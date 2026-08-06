#estrutura a base e visão geral
import tkinter as tk
from tkinter import ttk


root  = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("800x600")
#Label_ Imagens
minha_imagem = tk.PhotoImage(file="images.png")

label = tk.Label(root, image=minha_imagem)
label.pack(expand=True)



root.mainloop()