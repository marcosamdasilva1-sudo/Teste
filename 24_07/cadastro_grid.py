#EXEMPLO PRÁTICO - FORMULÁRIO COM GRID
#INTERFACE DE CADASTRO COMBINANDO LABEL, ENTRY, COMOBOBOX E BUTTON, TODOS POSICIONADOS COMO GRID
#ESTRUTURA DO FORMULÁRIO
#imagem de perfil posicionado na coluna com rowspam
#Labels e campos de entrada alinhados na coluna 1 e 2
# Botão "Enviar" fixado com sticky="e" a direita
#espaçamento uniforme com padx=5 e pady=5



import tkinter as tk
from tkinter import ttk
root  = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("400x400")


minha_imagem = tk.PhotoImage(file="profile.png").subsample(5, 5)
label = tk.Label(root, image=minha_imagem)
label.grid(row=0,column=0)

#campo label coluna1
label_nome 

root.mainloop()