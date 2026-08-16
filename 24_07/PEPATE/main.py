import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import random
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
#JOGADOR PESSOA
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


#JOGADOR PC
app_PC = Label(frame_cima, text="PC", height=1, anchor="center",
                    bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_PC.place(x=190, y=70)

#barra marcou pontos
app_PC_linha = Label(frame_cima, text="", height=10, anchor="center",
                         bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_PC_linha.place(x=250, y=0)


#pontuação
app_PC_pontos = Label(frame_cima, text="0", height=1, anchor="center",
                          bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_PC_pontos.place(x=190, y=20)

'''app_jogada_jogador = Label(frame_baixo="", height=1, anchor="center", bg=cor3, font="Ivy 10 bold")
app_jogada_jogador.place (x=10, y=10)

app_jogada_jogadorpc = Label(frame_baixo ="", height=1, anchor="center", bg=cor3, font="Ivy 10 bold")
app_jogada_jogadorpc.place (x=190, y=10)'''



icone_pedra = Image.open("pedra.png")
icone_pedra = icone_pedra.resize((50, 50), Image.Resampling.LANCZOS)
icone_pedra = ImageTk.PhotoImage(icone_pedra)
btn_pedra = tk.Button(frame_baixo, command=lambda:jogar("pedra"), width=50, height=50, image=icone_pedra, bg=cor5)
btn_pedra.place(x=15, y=60)


icone_papel = Image.open("papel.png")
icone_papel= icone_papel.resize((50, 50), Image.Resampling.LANCZOS)
icone_papel= ImageTk.PhotoImage(icone_papel)
btn_papel = tk.Button(frame_baixo, command=lambda:jogar("papel"), width=50, height=50, image=icone_papel, bg=cor5)
btn_papel.place(x=70, y=60)

icone_tesoura = Image.open("tesoura.png")
icone_tesoura = icone_tesoura.resize((50, 50), Image.Resampling.LANCZOS)
icone_tesoura = ImageTk.PhotoImage(icone_tesoura)  
btn_tesoura = tk.Button(frame_baixo, command=lambda:jogar("tesoura"), width=50, height=50, image=icone_tesoura, bg=cor5)
btn_tesoura.place(x=125, y=60)

#funcao iniciar jogo

'''def iniciar_jogo():
    global icone_pedra
    global icone_papel
    global icone_tesoura
    global btn_pedra
    global btn_papel
    global btn_tesoura

   



global escolha_pessoa
global escolha_pc
global pontos_pc
global rodadas
pontos_pessoa = 0 
pontos_pc = 0 
rodada = 5'''


#funcao logica do jogo

def jogar(escolha_pessoa):
    global pontos_pessoa
    global pontos_pc
    global rodadas
    opcoes = ["pedra", "Papel", "tesoura"]

    escolha_pc = random.choice(["pedra", "papel", "tesoura"])
    escolha _pc

    if rodadas > 0:
        print(rodadas)
        Escolha_pc = random.choice(opcoes)


    if escolha_pessoa == escolha_pc:
        resultado = "Empate!"
    elif (escolha_pessoa == "pedra" and escolha_pc == "tesoura") or (escolha_pessoa == "papel" and escolha_pc == "pedra") or (escolha_pessoa == "tesoura" and escolha_pc == "papel"):
        resultado = "Você ganhou!"
        pontos_pessoa += 1





janela.mainloop()
