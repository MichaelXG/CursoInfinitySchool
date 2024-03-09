print("""
    31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
        Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido 
        de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra.
        O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
        para então calcular e mostrar o valor do troco. 
        Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
        
        A saída deve ser conforme o exemplo abaixo:
       
        Lojas Tabajara 
        Produto 1: R$ 2.20
        Produto 2: R$ 5.80
        Produto 3: R$ 0
        Total: R$ 9.00
        Dinheiro: R$ 20.00
        Troco: R$ 11.00
        ...
""")
soma = 0.0
dinheiro = 0.0
troco = 0.0
cont = 1
cupom = []

cupom_al_top = \
("""
#-------------------------------------------#
#              Loja Tabajara                #
#-------------------------------------------#
""")
cupom_al_center = \
("""#            ... Cupom Fiscal ...           #""")

cupom_al_bootom = \
("""#-------------------------------------------#""")

print(cupom_al_top)
    
controle = -1 
while controle != 0:
    p = input(f'Informe o preço do produto_{cont}: R$ ')
    
    preco = float((p).replace(",", "."))
    cupom.append(f' Produto {cont}: R$ {"{:.2f}".format(preco)}')
    cont += 1

    if preco == 0:
        controle = 0

    # Soma dos números digitados    
    soma +=  preco
    
    if controle == 0:
        print(cupom_al_top + cupom_al_center)
        print('\n'.join(map(str, cupom)))
        print(f' Total: R$ {"{:.2f}".format(soma)}')
        print(cupom_al_bootom)

        while dinheiro <= 0 or dinheiro < soma:
            d = input(' Dinheiro: R$ ')
            
            dinheiro = float((d).replace(",", "."))
            
            if dinheiro > soma:
                troco = dinheiro - soma
        print(f' Troco : R$ {"{:.2f}".format(troco)}')
        print(cupom_al_bootom)
