import tkinter as tk
from tkinter import ttk


root  = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("900x900")
 #Listbox - Lista de opçoes
def selecao_mudou(evento):
    sel = evento.widget.curselection()
    if sel:
        idx = sel[0]
        label.config(text=f"{evento.widget.get(idx)} selecionado!")
listbox = tk.Listbox(root)
for item in ["primeiro", "Segundo", "Terceiro"]:
    listbox.insert(tk.END, item)
listbox.bind("<<ListboxSelect>>", selecao_mudou)
listbox.pack(expand=True)
label = tk.Label(root, text="Primeiro selecionado!")
label.pack()


root.mainloop()