from doctest import master

import customtkinter as ctk
from tkinter import messagebox


janela = ctk.CTk()
janela._set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#funções
def enviar():
    username = entrada_username.get()
    senha = entrada_senha.get()

    if username == "root" and senha == "12345":
        messagebox.showinfo("Login", "Login bem-sucedido")
    else:
        messagebox.showerror("Erro", "As informações estão erradas")


janela.geometry("500x400")
janela.title("Login")

ctk.CTkLabel(janela, text="Digite seu username").pack(pady=10)

entrada_username = ctk.CTkEntry(janela, corner_radius=32, width=200)
entrada_username.pack(pady=10)

ctk.CTkLabel(janela, text="Digite sua senha").pack(pady=10)

entrada_senha = ctk.CTkEntry(janela, width=200, corner_radius=32, show="*")
entrada_senha.pack(pady=10)



botao_enviar = ctk.CTkButton(master=janela,
                             text="Login",
                             command=enviar,
                             corner_radius=32)
botao_enviar.place(relx=0.5, rely=0.5, anchor="center")


botao_enviar.pack(pady=10)





janela.mainloop()