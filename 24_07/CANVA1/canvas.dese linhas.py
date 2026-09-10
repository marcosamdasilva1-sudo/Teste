from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x400")
Canvas = Canvas (janela, width=400, height=300, bg= "yellow")



Canvas.create_line (10, 10, 200, 200, fill = "black", width=3)
Canvas.create_line (10, 10, 10, 300, fill = "red", width=3)
Canvas.create_line (10, 10, 300, 10, fill = "blue", width=3)



Canvas.pack()
janela.mainloop()