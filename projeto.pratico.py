#projeto pratico - tela de login
#o que esse projeto demonstra , uma tela de login completa construida apenas com o geometry manager pack e seus parametros
#anchor="w"alinha os labels" Usuario e Senha" a esquerda
#side="left e side="right" posicionam os elementos no rodapé
#fill="x" no titulo faz o Label ocupar toda a largura
#ppady=5 aumenta a altura interna do título
#buscar a imagem em profile.png



mport tkinter as tk
from tkinter import messagebox 


root = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("900x900")
   
label1 = tk.Label(root, text = "LOGIN)")
label2 = tk.Label(root, text = "Faça se Login)") 
label3 = tk.Label(root, text = "Usuário")
label4 = tk.Label(root, text= "Senha")
lab
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

def button_command():
    try:
        peso = float(entry1.get())
        altura = float(entry2.get())

        imc = peso / (altura**2)



tk.Button(root, text="Top Button!").pack()
tk.Label(root, text="Hello, Left!").pack(side="left")
tk.Label(root,text="Hello, Right!").pack(side="right")
tk.Checkbutton(root, text="Uma opção na parte inferior!").pack(side=tk.BOTTOM)





root.mainloop()
