import tkinter as tk

#cria a janela principal
root = tk.Tk()

#cria um rótulo (label) com o texto "Hello, World"
message = tk.Label(root, text="bom dia, World")
message2 = tk.label(root, text= "Eu, tu, ele, nos")
#posiciona o rótulo na janela
message.pack()

#inicia o loop principal da interface gráfica
root.geometry("600x500+100+250")

root.mainloop()



