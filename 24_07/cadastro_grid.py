#EXEMPLO PRÁTICO - FORMULÁRIO COM GRID
#INTERFACE DE CADASTRO COMBINANDO LABEL, ENTRY, COMOBOBOX E BUTTON, TODOS POSICIONADOS COMO GRID
#ESTRUTURA DO FORMULÁRIO
#imagem de perfil posicionado na coluna com rowspam
#Labels e campos de entrada alinhados na coluna 1 e 2
# Botão "Enviar" fixado com sticky="e" a direita
#espaçamento uniforme com padx=5 e pady=5

import tkinter as tk
from tkinter import ttk, messagebox
root  = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("400x400")


minha_imagem = tk.PhotoImage(file="profile.png").subsample(5, 5)
label = tk.Label(root, image=minha_imagem)
label.grid(row=0,column=0, rowspan=5)

#campo label coluna1
#nome
label_nome = tk.Label(root, text="Nome")
label_nome.grid(row=0, column=1) 

entry_nome  = tk.Entry(root)
entry_nome.grid(row=0, column=2)

#genero

label_genero = tk.Label(root, text="Genero")
label_genero.grid(row=1, column=1) 

combobox_genero = ttk.Combobox(root, values=["Masculino", "Feminino"])
combobox_genero.grid(row=1, column=2)   

#cor dos olhos

label_olhos = tk.Label(root, text="Cor dos olhos")
label_olhos.grid(row=2, column=1) 


combobox_olhos = ttk.Combobox(root, values=["Castanho","Verdes","Azul","Negros"])
combobox_olhos.grid(row=2, column=2) 


#altura

label_altura = tk.Label(root, text="Altura")
label_altura.grid(row=3, column=1) 

entry_altura  = tk.Entry(root)
entry_altura.grid(row=3, column=2)

#Peso

label_peso = tk.Label(root, text="peso")
label_peso.grid(row=4, column=1) 

entry_peso  = tk.Entry(root)
entry_peso.grid(row=4, column=2)

#adicionar botao

def button_command():
    messagebox.showinfo("Você clicou no botão!")

button = tk.Button(root,text="Clique Aqui", command=button_command)
button.grid(row=5, column=2, sticky="e")





root.mainloop()