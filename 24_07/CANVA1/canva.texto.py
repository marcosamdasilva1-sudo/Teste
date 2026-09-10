from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("500x400")
Canvas = Canvas(janela, width=400, height=300, bg= "yellow")


#metodo

#canvas.create_text(200, 150, text="seu texto", font=("Arial",12), fill="blue")

#posicionamento, as coordenadas(x,y indicam o centro do texto no canvas. use-as para posicionar rotulos e títulos com precisão.
#exemplo), "bold" gera efeito de negrito na font, anchor trata do alinhamento do texto na pagina


Canvas.create_text(200, 100, text="olá", font=("Arial", 40), fill="blue" )

Canvas.create_text(200, 150, text="logica de programação", font=("Arial", 10), fill="green", anchor="w" )


Canvas.create_text(200, 200, text="logica de programação", font=("Arial", 10, "bold"), fill="black", anchor="e" )


Canvas.pack()
janela.mainloop()


