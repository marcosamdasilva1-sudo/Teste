from tkinter import *
from tkinter import ttk

#pip instal pillow


# import tkinter as tk
from tkinter import*
from tkinter import ttk

#cores--------------------------------------
cor0 = "#FFFFFF" # white /branco
cor1 = "#333333" # Black / preto
cor2 = "#fcc058" # Orange / laranja
cor3 = "#fff873" # yellow / amarelo
cor4 = "#34ed3d" # green / verde
cor5 = "#e85151" # red / vermelho
fundo = "#3b3b3b"  # 

janela = Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("260x280")
janela.configure(bg=fundo)

frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo=Frame(janela, width=260, height=300, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# CONFIGURANDO OS JOGADORES
#JOGADOR PESsOA

app_pessoa = Label(frame_cima, text="jogador", height=1, anchor="center",
                    bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=10, y=70)

#barra marcou pontos
app_pessoa_linha = Label(frame_cima, text="", height=10, anchor="center",
                         bg=cor4, fg=cor0, font=("Ivy 10 bold"))

app_pessoa_linha.place(x=0, y=0)


#pontuação

app_pessoa_pontos = Label(frame_cima, text="0", height=1, anchor="center",
                          bg=cor1, fg=cor0, font=("Ivy 30 bold"))

app_pessoa_pontos.place(x=50, y=20)

#separaçao da pontuação

app_vs = Label(frame_cima, text=":", height=1, anchor="center",
               bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125, y=20)




















#barra de empate
app_empate = Label(frame_cima, text="", width=255, anchor="center", bg=cor3)
app_empate.place(x=0, y=95)

#configura
janela.mainloop()
