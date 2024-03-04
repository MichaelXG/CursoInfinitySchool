# 1º comando : função system
from os import system

# 1º comando : função system
from time import sleep

numero = 30

while numero >= 0:
    if numero >= 10:    
        print(f'00:00:{numero}')
    else:
        print(f'00:00:0{numero}')
    numero -= 1
    sleep(0.75)
    system("cls")


