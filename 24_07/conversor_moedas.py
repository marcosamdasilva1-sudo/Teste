#atividade pratica, conversor de moedas
#o que desenvolver
#crie um app de conversao de moedas com interface grafica usando tkinter e grid
# 1 Campo de entrada - uusuario digita o valor da moeda
#2 selecao de moedas - comoboxes para origem e destino (ex BRL - USD)
#3 resultado formatado - exibir conversao em duas casas decimais

import tkinter as tk
from tkinter import ttk,messagebox

root  = tk.Tk()
root.title("Conversor Automatico de Moedas")
root.geometry("400x400")

# campo taxas

taxas={"USD":1.00,
       "JPY":157.00,
       "EUR":0.92,
       "BRL":5.50,
       "GBP":0.79}

#campo label valor 


label_valor = tk.Label(root, text="Valor")
label_valor.grid(row=0, column=0) 



entry_valor  = tk.Entry(root)
entry_valor.grid(row=0, column=1,sticky="ew")


#campo moedadeorigem

label_moedaorigem = tk.Label(root, text="Moeda de Origem")
label_moedaorigem.grid(row=1, column=0)

combobox_moedaorigem = ttk.Combobox(root, values=["USD","BRL","EUR","JPY"])
combobox_moedaorigem.grid(row=1, column=1,padx=5,pady=5) 



combobox_moedadestino = ttk.Combobox(root, values=["USD","BRL","EUR","JPY"])
combobox_moedadestino.grid(row=2, column=1,padx=5,pady=5) 

# campo funcao de conversao

def conversao():

    busca_valor=float(entry_valor.get().replace("," , "."))

    moeda_origem = combobox_moedaorigem.get()
    moeda_destino = combobox_moedadestino.get()

    #definir valor conversao

    valor_usd = busca_valor / taxas [moeda_origem]
    valor_destino = busca_valor * taxas[moeda_destino]

    label_resultado=tk.Label(f"{busca_valor:.2f} {moeda_origem} = {valor_destino:.2f} {moeda_destino}")
    label_resultado.grid(row=6,column=1)



#moeda destino

label_valor = tk.Label(root, text="Moeda de Destino")
label_valor.grid(row=2, column=0,padx=15,pady=15)


combobox_moedadestino = ttk.Combobox(root, values=["USD","BRL","EUR","JPY"])
combobox_moedadestino.grid(row=2, column=1,padx=15,pady=15) 

# campo conversão


#messagebox.showinfo("Informação", "Você recebeu um alerta!")

button= tk.Button(text="Converter", command=conversao)
button.grid(row=5, column=1)







 #converter
 




root.mainloop()