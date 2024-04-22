print("""
    [PY-A01] Faça um programa em python que determine em duas variáveis (senha e email) e que contenha 
            uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha 
            e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar 
            se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. 
            E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele 
            continue em um loop.
""")

# pip install pwinput
# instalar para poder usar mascara ao digitar senhas
import pwinput

email_db = 'python-a01@gmail.com'
senha_db = 'py-a01'

controle = True
while controle:
    email = str(input('Informe o e-mail de usuário: '))
    senha =  pwinput.pwinput(mask='*')
    if (email != email_db) or (senha != senha_db):
        print(f'Ops! Algo está errado. Tente novamente... \n' \
              'O e-mail ou senha inválidos. \n')
    
    else:
        controle = False
    
if not controle:   
    print('#-------------------------------------------------------#')
    print('E-mail e senha validos')
    print('#-------------------------------------------------------#')
