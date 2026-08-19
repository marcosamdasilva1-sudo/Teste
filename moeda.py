import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()
root.title("Conversor de Moedas")
root.geometry("300x150")
taxas = [
        "USD": 1.0
        "BRL": 5.50
        "EUR": 0.92
        "GBP": 0.79
        "JPY": 157.00]

label_valor =tk.Label(text="valor")
label_valor.grid(row=0, column=0, padx=5, pady=5)

entry_valor=tk.Entry()
entry_valor.grid(row=0, column=1, sticky="ew")

moeda_origem =tk.Label(text=(" Moeda de Origem"))
moeda_origem.grid(row=1,column=0, padx=10, pady=10) 

combobox = ttk.Combobox(root, values=["BRL", "USD", "EUR", "GBP", "JPY"])
combobox.grid(row=1, column=1)   

moeda_destino = tk.Label(text = "Moeda de Destino")
moeda_destino(row=2,collumn = 0, padx=10, pady= 10)






root.mainloop()

