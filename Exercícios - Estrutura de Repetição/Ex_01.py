print("""
    1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
       e continue pedindo até que o usuário informe um valor válido.
""")

controle = True

while controle:
    nota = int(input("Informe uma nota ente [0 - 10]: "))
    
    if nota < 0 or nota > 10:
        print("Ops! Algo está errado. Tente novamente... \n")
    else:
        controle = False

print('#-------------------------------------------------------#')
print(f'Nota valida : {"{:.2f}".format(nota)}')
print('#-------------------------------------------------------#')