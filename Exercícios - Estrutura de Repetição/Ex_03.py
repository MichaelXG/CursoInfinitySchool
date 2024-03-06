print("""
    3. Faça um programa que leia e valide as seguintes informações:
        a. Nome: maior que 3 caracteres;
        b. Idade: entre 0 e 150;
        c. Salário: maior que zero;
        d. Sexo: 'f' ou 'm';
        e. Estado Civil: 's', 'c', 'v', 'd';
""")
# a. Nome: maior que 3 caracteres;
nome = ''
while (len(nome) <= 3):
    nome = input('Informe um nome: ')
    if (len(nome) <= 3):
        print("Ops! Algo está errado. Tente novamente... \n"\
              "O nome deve ser maior que 3 caracteres. \n")

# print('#-------------------------------------------------------#')
# print(f'Nome: {nome}')
# print('#-------------------------------------------------------#')

# b. Idade: entre 0 e 150;
idade = -1
while (idade < 0) or (idade > 150):
    idade = int(input('Informe a idade: '))
    if (idade < 0) or (idade > 150):
        print("Ops! Algo está errado. Tente novamente... \n"\
              "A Idade deve estar entre 0 e 150. \n")
        
# print('#-------------------------------------------------------#')
# print(f'Idade: {idade}')
# print('#-------------------------------------------------------#')

# c. Salário: maior que zero;
salario = 0
while (salario <= 0):
    salario = float(input('Informe o salario: '))
    if (salario <= 0):
        print("Ops! Algo está errado. Tente novamente... \n"\
              "O salário deve ser maior que zero. \n")

# print('#-------------------------------------------------------#')
# print(f'Salário: R$ {"{:.2f}".format(salario)}')
# print('#-------------------------------------------------------#')

#  d. Sexo: 'f' ou 'm';
sexo = ''
while (sexo != 'F') and (sexo != 'M'):
    sexo = input('Informe o sexo: ').upper()
    if (sexo != 'F') and (sexo != 'M'):
        print("Ops! Algo está errado. Tente novamente... \n"\
              "O sexo deve ser infomado como 'M - masculino' ou 'F - feminino'. \n")        

# if sexo.upper() == 'F':
#     s = 'F - feminino'
# elif sexo.upper() == 'M':
#     s = 'M - masculino'
# print('#-------------------------------------------------------#')
# print(f'Sexo: {s}')
# print('#-------------------------------------------------------#')

#  e. Estado Civil: 's', 'c', 'v', 'd';
estado_civil = 'A'
while ('SCVD'.find(estado_civil) < 0):
    estado_civil = input('Informe o estado civil: ').upper()
    if ('SCVD'.find(estado_civil) < 0):
        print("Ops! Algo está errado. Tente novamente... \n"\
              "Estado civil deve ser informado como: \n"\
              "'S - Solteriro', 'C - Casado', 'V - Viúvo' ou 'D - Divorciado' \n")

# if estado_civil.upper() == 'S':
#     ec = 'S - Solteriro'
# elif estado_civil.upper() == 'C':
#     ec = 'C - Casado'
# elif estado_civil.upper() == 'V':
#     ec = 'V - Viúvo' 
# elif estado_civil.upper() == 'D':
#     ec = 'D - Divorciado'
       
# print('#-------------------------------------------------------#')
# print(f'Estado civil: {ec}')
# print('#-------------------------------------------------------#')
