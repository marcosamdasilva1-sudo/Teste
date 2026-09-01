from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x400")
canvas = Canvas(janela, width=700, height=400, bg= "yellow")




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
#x1 move para esquerda, y1 mexe na altura do quadrado,x2 move quadrado para direita,
# y2 move para cima ou para baixo, dimuindo a largura do quadrado 
canvas.create_rectangle(300,150,450,200, fill = "black")

# rodas do carro

canvas.create_oval(100,100, 250, 250, fill= "white")

#rodas do carro
canvas.create_oval(20,100, 250, 250, fill= "white")



# o codigo vai aqui


canvas.pack()
janela.mainloop()