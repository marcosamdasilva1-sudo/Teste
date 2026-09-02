from tkinter import Tk, canvas
janela = Tk()
janela.geometry("500x400")
canvas = canvas(janela, width=400, height=300, bg= "yellow")



canvas.create_rectangle(50, 50, 150, 100, fill = "blue")




canvas.pack()
janela.mainloop()
