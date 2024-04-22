
import metodos

notas_medias = [6.8, 8.0, 7.0, 8,7, 5.6, 6.9, 9.2, 8.4, 9.3, 10]

#Problema: Se o aluno > 7 foi aprovado, se tirou < 7 fo reprovado.

for nota in notas_medias:
  if nota >= 7:
    print('Aprovado')
  else:
    print('Reprovado')


# Dicionarios

perfil = {
    "nome"  : 'Michael'
  , "idade" : 38
  , "sexo"  : 'M'
  , "profissao" : 'Analista de sistemas'
}

print(f'{perfil["nome"]}')