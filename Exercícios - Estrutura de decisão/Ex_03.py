print("""
    3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
""")

# 'F' para FEMININO ou 'M' para MASCULINO.
sexo = input("Informe o sexo ('F' ou 'M'): ")
    
print('#---------------------------------------------------#')
if (sexo.upper() == 'M'):
    print(f'{sexo} - Masculino')
elif (sexo.upper() == 'F'):
    print(f'{sexo.upper()} - Feminino')
else:
    print(f'{sexo.upper()} - sexo invalido')
print('#---------------------------------------------------#')
    