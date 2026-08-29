from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x400")
canvas = Canvas(janela, width=400, height=300, bg= "yellow")




#parede
canvas.create_rectangle(50, 100, 250, 200, fill = "red")

#porta
canvas.create_rectangle(150, 120, 120, 200, fill = "black")

#jan esq
canvas.create_rectangle(80, 150, 100, 110, fill = "white")

#jan dir
canvas.create_rectangle(180, 150, 200, 110, fill = "orange")

#telhado
canvas.create_polygon(
 50, 100,
 150, 50, 
 250, 100,
 
 fill = "green"
 )

# carro


canvas.create_polygon(
 100, 100,
 60, 50, 
 110, 100,
 85, 150,
 35, 150,
 fill = "green"
 )




# o codigo vai aqui


canvas.pack()
janela.mainloop()