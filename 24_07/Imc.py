# Calcular o IMC
#Inserir o peso m Kg   - 80 kg
#Inserir a altura em metros - 1.90 m
#IMC - Multiplicar o peso  vezes altura
#exibir o resultado - Seu indice de massa corporal é ....




#estrutura a base e visão geral
import tkinter as tk
from tkinter import messagebox 


root = tk.Tk()
root.title("SENAI - Curso Técnico em Desenvolvimento de Sistemas")
root.geometry("900x900")
   
label1 = tk.Label(root, text = "Peso (Kg)")
label2 = tk.Label(root, text = "Altura (Metros)") 
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

def button_command():
    try:
        peso = float(entry1.get())
        altura = float(entry2.get())

        imc = peso / (altura**2)

        if imc <18.5: 
            resultado = "Abaixo do Peso"

        elif imc <25:
            resultado = "Peso Ideal" 

        elif imc <30:
            resultado = "sobrepeso"

        elif imc <35:
            resultado = "Obesidade grau 1"

        elif imc <40:
            resultado = "Obesidade grau 2"

        else:
            resultado = "Obesidade grau 3"
        label3.config(text=f"IMC {imc:.2f}\n{resultado}")

    except ValueError:
        label3.config(text= " o valor inserido errado")
        return
        


label3 = tk.Label(root, text =  "")





button = tk.Button(root,text="Calcular", command=button_command)
    

   

label1.pack()
entry1.pack()

label2.pack()
entry2.pack()

button.pack()

label3.pack()

root.mainloop()