# criando um frame basico
# o codigo abaixo demosntra como criar e exibir um frame simples usando o método pack() com margens externas definidas por pack e pady

import  tkinter as tk

root = tk.Tk()
root.title ("SENAI - Desenvolvimento de Sistems")
root.config(bg="skyblue")

frame = tk.Frame(root, width=200, heigth=200)
frame.pack(padx=10, pady=10)
           
root.mainloop()