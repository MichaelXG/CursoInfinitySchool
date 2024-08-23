print("""
    26. Numa eleição existem três candidatos. 
        Faça um programa que peça o número total de eleitores. 
        Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
""")

# 1º comando : função system
from os import system

total_nulos = total_candidato_01 = total_candidato_02 = total_candidato_03 = 0
maior_votacao = 0
eleito = ''
urna_al_top = \
("""
#-------------------------------------------#
#             Urna Eletrônica               #
""")
urna_candidatos = \
("""
#-------------------------------------------#
#           ... Candidatos ...              #
#                                           #
#   0 - Nullo                               #
#   1 - Zé das Couves                       #
#   2 - Pé de pano                          #
#   3 - Tião Galinha                        #
#-------------------------------------------#
#                                           #
""")

urna_al_bottom = \
("""
#                                           #
#-------------------------------------------#
""")

qtd_eleitores = 0
while qtd_eleitores <= 0:
    qtd_eleitores = int(input('Informe o número total de eleitores: '))
    if qtd_eleitores <= 0:
        print('Quantidade deve ser maior que zero!')

votos_urna = []

while len(votos_urna) != qtd_eleitores:
    voto = input(f'{urna_al_top}{urna_candidatos}#  Digite o número do candidato :           #{urna_al_bottom}\nEleitor: {len(votos_urna) + 1}\nSeu Voto: ')
    votos = int(voto)
    votos_urna.append(votos)
    
    if votos < 0 or votos > 3:
        print("Ops! número incoreto ...\nEste candidato não existe. \n")
        votos_urna.remove(votos)
    else:
        if votos == 0:
            total_nulos += 1
        elif votos == 1:
            total_candidato_01 += 1
        elif votos == 2:   
            total_candidato_02 += 1 
        elif votos == 3:   
            total_candidato_03 += 1 
     
    system("CLS")        
maior_votacao =  total_candidato_01
eleito = ' O candidato eleito é 1 - Zé das Couves'

if total_candidato_02 > maior_votacao:
    maior_votacao = total_candidato_02
    eleito = 'O candidato eleito é 2 - Pé de pano'
if total_candidato_03 > maior_votacao:
    maior_votacao = total_candidato_03  
    eleito = 'O candidato eleito é 3 - Tião Galinha'

if total_candidato_01 == total_candidato_02 and total_candidato_01 == total_candidato_03:
    eleito = 'Empate eleição anulada                 '
# print(f'\nVotação: {votos_urna}')

print(f'{urna_al_top}\
#-------------------------------------------#\
\n#              Apuração votos               #\
\n#-------------------------------------------#\
\n#                                           #\
\n#   00 - Votos Nulos      = {total_nulos}               #\
\n#   10 - Zé das Couves    = {total_candidato_01}               #\
\n#   11 - Pé de pano       = {total_candidato_02}               #\
\n#   12 - Tião Galinha     = {total_candidato_03}               #\
\n#-------------------------------------------#\
\n#               Parabéns                    #\
\n#                                           #\
\n#   {eleito} #\
{urna_al_bottom}\n')