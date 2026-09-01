import tkinter as tk
from tkinter import ttk
root = tk.Tk()

#cores
#1ª faixa refere-se ao algarismo significativo de cada cor

def faixa1_cor():

    if faixa1_cor == "preto":
        return 0

    elif faixa1_cor =="marrom":
        return  1

    elif faixa1_cor == "vermelho":
        return  2

    elif faixa1_cor =="laranja":
        return 3

    elif faixa1_cor == "amarelo":
        return 4

    elif faixa1_cor =="verde":
        return 5

    elif faixa1_cor =="azul":
        return 6

    elif faixa1_cor =="violeta":

        return 7
    elif faixa1_cor =="cinza":
        return 8

    elif faixa1_cor =="branco":
        return 9

    else:
      print("mensagem invalida")


#2ª faixa refere-se ao algarismo significativo da cada cor 

def faixa2_cor():

    if faixa2_cor == "preto":
        return 0
    
    elif faixa2_cor =="marrom":
       return  1
    
    elif faixa2_cor == "vermelho":
        return  2
    
    elif faixa2_cor =="laranja":
        return 3
    
    elif faixa2_cor == "amarelo":
        return 4
    
    elif faixa2_cor =="verde":
        return 5
    
    elif faixa2_cor =="azul":
        return 6
    
    elif faixa2_cor =="violeta":
        return 7

    elif faixa2_cor =="cinza":
        return 8
    
    elif faixa2_cor =="branco":
        return 9
    
    else:
        print("mensagem invalida")
    
#3ª faixa refere-se a quantidade de zeros

def faixa3_cor():
    
    if faixa3_cor == "preto":
        return 0
    
    elif faixa3_cor=="marrom":
       return  1
    
    elif faixa3_cor == "vermelho":
        return  2
    
    elif faixa3_cor =="laranja":
        return 3
    
    elif faixa3_cor == "amarelo":
        return 4
    
    elif faixa3_cor =="verde":
        return 5
    
    elif faixa3_cor =="azul":
        return 6
    
    elif faixa3_cor =="violeta":
        return 7

    elif faixa3_cor=="cinza":
        return 8
    
    elif faixa3_cor =="branco":
        return 9
    
    else:
        print("mensagem invalida")
    

# 4ª faixa refere-se a tolerância em porcentagem variando aproximadamente em  == 5/100, para cima ou para baixo

def faixa_tolerancia():

    if faixa_tolerancia == "ouro":
        return 0.05
    
    elif faixa_tolerancia =="prata":

        return 0.10

# box vamos ter o valor do resistor

#faixa dourada ==5/100
#faixa prata == 10/100
#faixa branca == 20/100

def fator_multiplicadordecores():

    if faixa3_cor == "preto":
        return 1
        
    elif faixa3_cor=="marrom":
        return  100
        
    elif faixa3_cor == "vermelho":
        return  1000
        
    elif faixa3_cor =="laranja":
        return 10000
        
    elif faixa3_cor == "amarelo":
        return 100000
        
    elif faixa3_cor =="verde":
        return 1000000
        
    elif faixa3_cor =="azul":
        return 10000000
        
    elif faixa3_cor =="violeta":
        return 100000000
    
    elif faixa3_cor=="cinza":
        return 1000000000
        
    elif faixa3_cor =="branco":
        return 10000000000

    






root.mainloop()




