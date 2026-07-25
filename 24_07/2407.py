import tkinter as tk
#cria a janela principal
root = tk.TK()

#cria um rótulo (label) com o texto "Hello, World"
message = tk.Label(root, text="Hello, World")

#posiciona o rótulo na janela
message.pack()

#inicia o loop principal da interface gráfica
root.mainloop()