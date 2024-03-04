print("""
   10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
)
celsius = float(input('Informe a temperatura em graus Celsius: '))

def convertFahrenheitCelsius(celsius):
   fahrenheit = ((celsius * 9) / 5) + 32
   return fahrenheit

print(f'{convertFahrenheitCelsius(celsius)} graus Fahrenheit')
