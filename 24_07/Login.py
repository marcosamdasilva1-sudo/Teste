import tkinter as tk
from tkinter import ttk


root  = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("900x900")
#campo login

label_login = tk.Label(root, text = "Faça seu Login", font=("ivy", 20))
label_login.pack(ipady=5, fill="x")


# campo imagem
minha_imagem = tk.PhotoImage(file="profile.png").subsample(5, 5)
label = tk.Label(root, image=minha_imagem)
label.pack()

#campo usuario

frame_usuario = tk.Frame(root)
frame_usuario.pack(anchor ="w")

label_usuario = tk.Label(root, text = "Usuário")
label_usuario.pack(side = "left", padx = 50)

entry  = tk.Entry(root)
entry.insert(0, "Insira seu Nome")
entry.pack()


label = tk.Label(root, text="Demonstração!")
label.pack()

#campo senha
frame_senha = tk.Frame(root)
frame_senha.pack(anchor ="w")

label_usuario = tk.Label(root, text = "Usuário")
label_usuario.pack(side = "left", padx



label_usuario
# O CODIGO VAI AQUI



tk.Label(root,text="senha")

root.mainloop()