import tkinter as tk
from tkinter import Tk,Canvas
janela = Tk()
from tkinter import ttk
root  = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("500x500")
janela.geometry("600x400")
Canvas =Canvas(janela, width=600, height=400, bg= "white")


#cores
#1ª faixa refere-se ao algarismo significativo de cada cor

def faixa1_cor(cor):

    if cor == "preto":
        return 0

    elif cor =="marrom":
        return  1

    elif cor == "vermelho":
        return  2

    elif cor =="laranja":
        return 3

    elif cor == "amarelo":
        return 4

    elif cor =="verde":
        return 5

    elif cor =="azul":
        return 6

    elif cor =="violeta":

        return 7
    
    elif cor =="cinza":
        return 8

    elif cor =="branco":
        return 9

    else:
      print("escolha opçao válida")


#2ª faixa refere-se ao algarismo significativo da cada cor 

def faixa2_cor(cor):

    if cor == "preto":
        return 0
    
    elif cor =="marrom":
       return  1
    
    elif cor == "vermelho":
        return  2
    
    elif cor =="laranja":
        return 3
    
    elif cor == "amarelo":
        return 4
    
    elif cor =="verde":
        return 5
    
    elif cor =="azul":
        return 6
    
    elif cor =="violeta":
        return 7

    elif cor =="cinza":
        return 8
    
    elif cor =="branco":
        return 9
    
    else:
        print("mensagem invalida")
    
#3ª faixa refere-se a quantidade de zeros

def faixa3_cor(cor):
    
    if cor == "preto":
        return 0
    
    elif cor=="marrom":
       return  1
    
    elif cor == "vermelho":
        return  2
    
    elif cor =="laranja":
        return 3
    
    elif cor == "amarelo":
        return 4
    
    elif cor =="verde":
        return 5
    
    elif cor =="azul":
        return 6
    
    elif cor =="violeta":
        return 7

    elif cor=="cinza":
        return 8
    
    elif cor =="branco":
        return 9
    
    else:
        print("mensagem invalida")
    


# box vamos ter o valor do resistor

#faixa dourada ==5/100
#faixa prata == 10/100
#faixa branca == 20/100

def fator_multiplicadordecores(cor):

    if cor == "preto":
        return 1
        
    elif cor=="marrom":
        return  100
        
    elif cor == "vermelho":
        return  1000
        
    elif cor =="laranja":
        return 10000
        
    elif cor == "amarelo":
        return 100000
        
    elif cor =="verde":
        return 1000000
        
    elif cor =="azul":
        return 10000000
        
    elif cor =="violeta":
        return 100000000
    
    elif cor=="cinza":
        return 1000000000
        
    elif cor =="branco":
        return 10000000000

# 4ª faixa refere-se a t
# tolerância em porcentagem variando aproximadamente em  == 5/100, para cima ou para baixo

def faixa_tolerancia(cor):

    if cor == "marrom":
        return 0.01
    
    elif cor =="verde":

        return 0.05

    elif cor =="azul":

        return 0.0025

    elif cor =="violeta":

        return 0.001

    elif cor =="cinza":

        return 0.0005

    elif cor =="dourado":
    
        return 0.0005

    elif cor =="prateado":
    
        return 0.1


combobox1 = ttk.Combobox(root, values=["preto", "marrom", "vermelho", "laranja", "amarelo", "verde", "azul", "violeta", "cinza", "branco"])
combobox1.grid(row=0, column=1)
tk.Label(root, text="1ª Faixa").grid(row=0, column=0)

combobox2 = ttk.Combobox(root, values=["preto", "marrom", "vermelho", "laranja", "amarelo", "verde", "azul", "violeta", "cinza", "branco"])
combobox2.grid(row=1, column=1)
tk.Label(root, text="2ª Faixa").grid(row=1, column=0)

combobox3 = ttk.Combobox(root, values=["preto", "marrom", "vermelho", "laranja", "amarelo", "verde", "azul", "violeta", "cinza", "branco"])
combobox3.grid(row=2, column=1)
tk.Label(root, text="3ª faixa").grid(row=2, column=0)

combobox4 = ttk.Combobox(root, values=["marrom", "verde", "azul", "violeta", "cinza", "dourado", "prateado"])
combobox4.grid(row=3, column=1)
tk.Label(root, text="tolerância").grid(row=3, column=0)


resultado = tk.Label(root, text="")
resultado.grid(row=6, column=0, columnspan=2)


def calcular():
    cor1 = combobox1.get()
    cor2 = combobox2.get()
    cor3 = combobox3.get()
    cor4 = combobox4.get()

    numero = faixa1_cor(cor1) *10 + faixa2_cor(cor2) 
    resistencia = numero * faixa3_cor (cor3) 
    tolerancia = faixa_tolerancia(cor4) 
    variacao_minima = resistencia - (resistencia * tolerancia / 100)
    variacao_maxima = resistencia + (resistencia * tolerancia /100)
    resultado.config(
            text=f"Resistencia{resistencia}Ω ±{tolerancia}%"

    )





button = tk.Button(root,text="calcular resistencia", command=calcular).grid(row=5,column=1)









Canvas.create_rectangle(50, 50, 350, 100, fill = "orange")

Canvas.create_line (125, 25, 50, 100, fill = "black", width=3)
Canvas.create_line (125, 125, 50, 500, fill = "black", width=3)


Canvas.pack()







     
  


root.mainloop()





