from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x400")
Canvas = Canvas(janela, width=400, height=300, bg= "yellow")



Canvas.create_rectangle(50, 50, 150, 100, fill = "blue")




Canvas.pack()
janela.mainloop()
