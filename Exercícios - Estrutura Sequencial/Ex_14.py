print("""
   14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
       Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
       deve pagar uma multa de R$ 4,00 por quilo excedente. 
       João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
       Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
       Imprima os dados do programa com as mensagens adequadas.
"""
)

quilos = float(input('Informe o peso dos peixes (quilos): '))

quilosLimite = 50
multaQuilo   = 4.00

if quilos > quilosLimite:
    quilosExedido = quilos - quilosLimite
    valorMulta    = quilosExedido * multaQuilo

    print('#---------------------------------------------------#')
    print(f'Peso dos peixes : {"{:.2f}".format(quilos)} KG')
    print(f'Quilo excedente : {"{:.2f}".format(quilosExedido)} KG')
    print(f'Valor da multa quilo excedente : R$ {"{:.2f}".format(valorMulta)}')
    print('#---------------------------------------------------#')
else:
    print(f'Não há multas para o peso')

