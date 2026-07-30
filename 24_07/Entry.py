#estrutura a base e visão geral
import tkinter as tk
from tkinter import ttk


root  = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("900x900")
#Entry _ Campo de texto

def enter_pressionado(event):
    label.config(text=event.widget.get())

entry  = tk.Entry(root)
entry.insert(0, "Digite seu texto")
entry.bind("<Return>", enter_pressionado)
entry.pack()


label = tk.Label(root, text="Demonstração!")
label.pack()

root.mainloop()