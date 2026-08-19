import tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("375x200")

foto = tk.photoimage(file="login.png").subsample(3,3)

foto_label=tk.Label(root,image=foto)
foto_label.grid(row=0, column=1, rowspan=5)

