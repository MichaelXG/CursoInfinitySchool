print("""
    8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
       sabendo que a decisão é sempre pelo mais barato.
""")
# 
p1 = float(input("Informe o preço 01: "))
p2 = float(input("Informe o preço 02: "))
p3 = float(input("Informe o preço 03: "))

if (p1 == p2) and (p1 == p3):
    msg = f'Os preços são iguais {"{:.2f}".format(p1)} '
elif (p1 < p2) and (p1 < p3):
    msg = f'O preço mais barato é {"{:.2f}".format(p1)} '
elif (p2 < p3):
    msg = f'O preço mais barato é {"{:.2f}".format(p2)} '
else:
        msg = f'O preço mais barato é {"{:.2f}".format(p3)} '
    
print('#---------------------------------------------------#')
print(msg)
print('#---------------------------------------------------#')