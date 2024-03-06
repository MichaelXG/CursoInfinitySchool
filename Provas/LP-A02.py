print("""
    [LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, 
             exiba uma mensagem dizendo que o usuário foi multado e o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.
""")

velocidade = float(input('Informe a a velocidade do carro: '))

limite_velocidade = 80
valor_multa = 20
valor_infracao = 0

if velocidade >  limite_velocidade:
    limite_exedito = velocidade - limite_velocidade
    valor_infracao = limite_exedito * valor_multa 
    msg = f'A velocidade de {velocidade} km/h exceder o limite permitido.\nVocê sera multado.'
else:
    msg = f'A velocidade de {velocidade} km/h está dentro do limite.'
    
print('#-------------------------------------------------------#')
print(msg)
print(f'Valor da multa : R$ {"{:.2f}".format(valor_infracao)}')
print('#-------------------------------------------------------#')

