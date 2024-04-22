alunos = [ 'Ana', 'Amanda', 'Carlos', 'Eduardo', 'Helena', 'Juliana', 'Viviane', 'Taysa', 'José', 'Victor']

notas = [ 8, 5.5, 7.4, 8.2, 9, 7.2, 6.8, 7, 8.4, 10] 
  
tamanho = len(alunos)
boletim_final = {}
for a in range(tamanho):
    # for n in range(tamanho_notas):
    boletim_final[a]= {'nome': f'{alunos[a]}','nota': notas[a]}
    

# print(boletim_final)


t = len(boletim_final)
for ap in range(t):
    boletim_final[ap]['Aprovado']= boletim_final[ap]['nota'] >= 7
   
# print(boletim_final)  


## Imprimir os nomes dos alunos aprovados.
## Imprimir a média total dos alunos da turma.



t = len(boletim_final)
for ap in range(t):
    if boletim_final[ap]['Aprovado'] == True:
        print(boletim_final[ap]['nome'])  


def calcular_media(valor, qtd) :
    media = (valor / qtd)
    return media 

t = len(boletim_final)
valor = 0
for ap in range(t):
    valor = valor + boletim_final[ap]['nota'] 

## Imprimir a média total dos alunos da turma.
media = calcular_media(valor, t)
print(f'Media : {media}')

## Remover a chave 'Aprovado'

t = len(boletim_final)
for ap in range(t):
    boletim_final.pop('Aprovado')  
    
print(boletim_final) 