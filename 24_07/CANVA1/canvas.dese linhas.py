from tkinter import Tk, canvas
janela = Tk()
janela.geometry("500x400")
canvas = canvas(janela, width=400, height=300, bg= "yellow")



canvas.create_line (10, 10, 200, 200, fill = "black", width=3)
canvas.create_line (10, 10, 10, 300, fill = "red", width=3)
canvas.create_line (10, 10, 300, 10, fill = "blue", width=3)



canvas.pack()
janela.mainloop()