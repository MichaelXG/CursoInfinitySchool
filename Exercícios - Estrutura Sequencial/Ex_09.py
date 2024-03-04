print("""
    9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
       C = 5 * ((F-32) / 9).
"""
)
grausFahrenheit = float(input('Informe a temperatura em graus Fahrenheit: '))

def convertFahrenheitCelsius(grausFahrenheit):
   celsius =  5 * ((grausFahrenheit-32) / 9)
   return celsius

print(f'{convertFahrenheitCelsius(grausFahrenheit)} graus Celsius')
