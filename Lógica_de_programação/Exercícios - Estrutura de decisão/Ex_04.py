print("""
    4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante
""")

# 
letra = input('Informe uma letra: ')
validaLetra = False

if ('AEIOU'.find(letra.upper()) >= 0):
    validaLetra = True
    
print('#---------------------------------------------------#')
if validaLetra:
    print(f'"{letra.upper()}" é vogal')
else:
    print(f'"{letra.upper()}" é consoante')
print('#---------------------------------------------------#')
    