#atividade pratica, conversor de moedas
#o que desenvolver
#crie um app de conversao de moedas com interface grafica usando tkinter e grid
# 1 Campo de entrada - uusuario digita o valor da moeda
#2 selecao de moedas - comoboxes para origem e destino (ex BRL - USD)
#3 resultado formatado - exibir conversao em duas casas decimais

import tkinter as tk
from tkinter import ttk

root  = tk.Tk()
root.title("conversor de moedas")
root.geometry("900x900")

#campo label conversor 
#nome

label_conversor = tk.Label(root, text="valor")
label_conversor.grid(row=0, column=0) 

entry_conversor  = tk.Entry(root)
entry_conversor.grid(row=0, column=1)


#campo valor


label_valor = tk.Label(root, text="moeda de origem")
label_valor.grid(row=1, column=0)

combobox_moedaorigem = ttk.Combobox(root, values=["USD","BRL","EUR","JPY"])
combobox_moedaorigem.grid(row=1, column=2)   


root.mainloop()