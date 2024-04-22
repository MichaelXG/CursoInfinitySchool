print("""
    36 - Crie um algoritmo que ao ser executado recebe uma palavra, verifica se a palavra se inicia com uma vogal
         e exibe a mensagem "Começa em vogal" caso a palavra se inicie em vogal
         ou exibe a mensagem "Começa em consoante" caso a palavra não se inicie em vogal

""")

palavra = input('Informe uma palavra: ')
validaLetra = False

if ('AEIOU'.find(palavra[0].upper()) >= 0):
    valida_palavra = True
    
print('#---------------------------------------------------#')
if valida_palavra:
    print(f'A primeira letra da palvara "{palavra.upper()}" é vogal')
else:
    print(f'A primeira letra da palvara "{palavra.upper()}" é consoante')
print('#---------------------------------------------------#')
    