print("""
    2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
       mostrando uma mensagem de erro e voltando a pedir as informações.
""")
# pip install pwinput
# instalar para poder usar mascara ao digitar senhas
import pwinput

controle = True

while controle:
    usuario = input('Informe um nome de usuário: ')
    senha =  pwinput.pwinput(mask='*')
    if (usuario == senha):
        print("Ops! Algo está errado. Tente novamente... \n"\
              "A senha não pode ser igual ao nome do usuário. \n")
    else:
        controle = False


print('#-------------------------------------------------------#')
print('Usuário e senha validos')
print('#-------------------------------------------------------#')