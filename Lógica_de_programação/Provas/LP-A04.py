print("""
   [LP-A04] ENTREGUE SEU PROJETO ABAIXO SEGUINDO AS OBSERVAÇÕES 
            
        SUGESTÃO DE PROJETO:

        SIMULADOR DE CADASTRO DE SENHA E INICIALIZAÇÃO DE CELULAR

        Utilizando o aprendizado desta aula, implementaremos um sistema de cadastro de senha e inicialização do celular 
        utilizando o loop "for".

        1. Após ligar o celular, o usuário é solicitado a inserir a senha cadastrada.
        2. São permitidas 3 tentativas até que o telefone seja bloqueado.
        3. Se o usuário acertar a senha, uma mensagem de boas-vindas é exibida: "Bem-vindo."
        4. Se o usuário errar a senha, uma mensagem informando o erro é exibida, 
           junto com o número de tentativas restantes até o bloqueio do telefone.
           
        Pense em todas as possibilidades e faça um sistema completo.
""")
# pip install pwinput
# instalar para poder usar mascara ao digitar senhas
import pwinput
# 1º comando : função system
from os import system
# 1º comando : função system
from time import sleep

tentativas = 3
cont_tentativas = 0
tentativas_restantes = 0
controle_senha = True
controle_tentativas = True
senha_padrao = 'soeu'

def ligar():
    ligar_celular = 'N' 
    while ligar_celular != 'S':
        ligar_c = input(f'{celular_al_top}#        Ligar o celular (S/N):            #{celular_al_bottom}\nResposta: ').upper()
        if ligar_c == 'S':
            ligar_celular = 'S' 
        else:
            system("CLS")   
            
def desligar():
    desligar_celular = 'N' 
    while desligar_celular != 'S':
        desligar_c = input(f'{celular_al_top}#        Desligar o celular (S/N):          #{celular_al_bottom}\nResposta: ').upper()
        if desligar_c == 'S':
            desligar_celular = 'S' 
        else:
            system("CLS")   
                       
def cronometro(tempo = 30, erro = 0, tentativa = 0): 
    while tempo >= 0:
        print(celular_al_top)
        if erro == 301:
            print("Preparando celular para desligar\n")
        elif erro == 401:
            print(f'Ops! Algo está errado. Tente novamente...\nA senha está incorreta.\nRestão apenas {tentativa} tentativas. \n')
        elif erro == 402:
            print("Ops! Algo está errado. Telefone bloqueado ...\nNúmero de tentativas execido. \n")
        
        if tempo >= 10:    
            print(f'Aguarde 00:00:{tempo} segundos')
        else:
            print(f'Aguarde 00:00:0{tempo} segundos')
        print(celular_al_bottom)
        tempo -= 1
        sleep(0.75)
        system("cls")

celular_al_top = \
("""
#------------------------------------------#
#                  Celular                 #
#------------------------------------------#
#                                          #
""")

celular_al_bottom = \
("""
#                                          #
#------------------------------------------#
""")

# Ligar  o celular
ligar()

while controle_senha:
    senha_celular =  pwinput.pwinput(mask='*')
    if (senha_celular != senha_padrao):
        cont_tentativas +=1
        tentativas_restantes =  tentativas - cont_tentativas
          
        if cont_tentativas == tentativas:
            controle_tentativas = False    
            controle_senha = False 
            
        cronometro(5, 401, tentativas_restantes)     
        print(celular_al_top)
    else:
        controle_senha = False
        
if not controle_tentativas:
    cronometro(5, 402)
    # caso informe a senha errada 3 vezes, para que não exina
    # a mensagem de bem vindo
    controle_senha = True
    # Desligar o celular
    desligar()
    cronometro(10, 301) 
    
# se informar a senha correta    
if controle_senha == False:
    system("CLS")  
    print(f'{celular_al_top}#                Bem Vindo ...             #{celular_al_bottom}\n ')