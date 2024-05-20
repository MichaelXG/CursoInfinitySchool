print("""
      [PY-A10] Usando seus conhecimentos aprendidos em sala, realize uma interface de login 
      utilizando a biblioteca Tkinter em Python. 
      O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se 
      o e-mail contiver o caractere "@", ou seja, realizar uma tela de login com restrições de e-mail e senha.
      """)
from tkinter import *
from tkinter import messagebox

def login():
    email = input_email.get()
    senha = input_senha.get()

    msg = ''

    # Verifica se a senha tem mais de 6 caracteres e se o e-mail contém "@"
    if len(senha) < 6:
        msg += 'Senha deve conter mais de 6 dígitos. \n'
    if "@" not in email:
        msg += 'E-mail inválido, faltando "@". \n'

    # Verifica se houve algum erro na validação
    if msg == '':
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
    else:
        messagebox.showerror("Login", f"Ops... algo deu errado... \n Por favor, verifique seu e-mail e senha! \n {msg}")

# Criar a janela principal
janela = Tk()
janela.geometry("400x300")
janela.title("Logins")

# E-mail
txt_email = StringVar()
Label(janela, text="E-mail:").grid(row=0, column=0, padx=10, pady=5)
input_email = Entry(janela, width=50, textvariable=txt_email, bg='lightgrey')
input_email.grid(row=0, column=1, padx=10, pady=5)

# Senha
txt_senha = StringVar()
Label(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=5)
input_senha = Entry(janela, show="*", width=50, textvariable=txt_senha, bg='lightgrey')
input_senha.grid(row=1, column=1, padx=10, pady=5)

# Botão login
btn_login = Button(janela, text="Cadastrar", command=login)
btn_login.grid(row=2, column=0, padx=10, pady=10, sticky=W)

janela.mainloop()
