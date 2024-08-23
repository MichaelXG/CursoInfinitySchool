print("""
    18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
        calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
)

arquivoMB = float(input('Informe o tamanho do arquivo para download (em MB): '))
velocidadeMbps = float(input('Informe a velocidade de um link de Internet (em Mbps): '))

def calculaTempoSownload(mb, mbps):
    tempo = (round(mb / mbps) * 60)
    return tempo

print('#---------------------------------------------------#')
print(f'Tempo aproximado de download: {calculaTempoSownload(arquivoMB,velocidadeMbps)} minutos \n')
print('#---------------------------------------------------#')
