#cuidados com o place desafios do posionamento absoluto
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("300x300+50+100")


def mostrar_selecao(event):
    selecao = cidades.curselection()
    messagebox.showinfo("Seleção", cidades.get(selecao))

tk.Label(root, text="Qual cidade voce gostaria de conhecer").place(x=50, y=20)

cidades = tk.Listbox(root, selectmode=tk.BROWSE, width=24)
cidades.place(x=40, y=65)

for cidade in ["Brasilia", "Florianóplois", "Porto Alegre", "Rio de Janeiro", "São Paulo"]:
    cidades.insert(tk.END, cidade)

cidades.bind("<<ListboxSelect>>", mostrar_selecao)

botao = tk.Button(root, text="Sair", command=quit)
botao.place(x=125, y=250)


root.mainloop()