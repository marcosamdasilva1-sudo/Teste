#estrutura a base e visão geral
import tkinter as tk
from tkinter import ttk


root  = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("900x900")

#Spinbox _ Entrada Numérica
#StringVar é uma variavel que armazena uma string
# é usada para atualizar widget dinamicamente

spinbox_var = tk.StringVar(value="0")

spinbox = tk.Spinbox(root,
    from_=-10,
    to=10,
    #increment=5,
    textvariable=spinbox_var)

spinbox.pack(expand=True)

label = tk.Label(root, textvariable=spinbox_var)
label.pack()




root.mainloop()