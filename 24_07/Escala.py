#estrutura a base e visão geral
import tkinter as tk
from tkinter import ttk


root  = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("900x900")
# Scale _ Controle Deslizante

def valor_mudou(evento):
    label.config(text=evento)

scale = tk.Scale(root,
    from_=0,
    to=10,
    orient="vertical",
    command=valor_mudou)
scale.pack()

label = tk.Label(root, text="0")
label.pack()

root.mainloop()