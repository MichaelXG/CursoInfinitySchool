controle = True

while controle:
    # @, provedor e pelo menos 15 caracteres
    email = input("Informe seu e-mail: ")

    if "@" not in email or len(email) < 15:
        print("Ops! Algo está errado. Tente novamente...")
    else:
        controle = False

print(f"O e-mail {email} está correto")