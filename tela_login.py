#Importar biblioteca
import tkinter as tk
from tkinter import messagebox


def fazer_login() :
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    #Verificar se o Usuario e a senha estão corretos
    if usuario == "Felipe" and senha == "2207" :
        messagebox.showinfo("Login","Login bem Sucedido")
    else :
        messagebox.showerror("Login","Senha invalida")


#Criado Janela
janela = tk.Tk()
janela.title("janela de login")

#Rotulo de Usuario
usuario_label = tk.Label(janela, text="Usuario: ")
usuario_label.pack();

#Campo de Entrada do Usuario
usuario_entry = tk.Entry(janela)
usuario_entry.pack()

#Rotulo de Senha
senha_label = tk.Label(janela, text="Senha: ")
senha_label.pack();

#Campo de Entrada de Senha
senha_entry = tk.Entry(janela,show="*")
senha_entry.pack()

#botão login
login_button = tk.Button(janela, text="login", command=fazer_login)
login_button.pack()

#iniciando a interface grafica
janela.mainloop()

