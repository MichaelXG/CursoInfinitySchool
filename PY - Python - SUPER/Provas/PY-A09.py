print("""
      [PY-A09] Desenvolva um código utilizando seus conhecimentos de Tkinter para converter 
      uma unidade de medida de centímetros para metros.
      """)

import tkinter as tk

def converter_cm_m():
    try:
        centimetros = float(input_cm.get())
        metros = centimetros / 100
        
        # Resultado da conversão
        label.config(text=f"{float(input_cm.get()):.2f} cm, convertidos em metros é: {metros:.2f} m")
    except ValueError:
        # Tratamento de erro
        label.config(text="Por favor, informe um valor válido!")

# Janela principal
janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")

# Label Informativo
label_centimetros = tk.Label(janela, text="Informe o valor em centímetros:")
label_centimetros.pack(pady=10)

# Input do valor em centímetros
input_cm = tk.Entry(janela)
input_cm.pack(pady=5)

# Botão para conversão
btn_converter = tk.Button(janela, text="Converter", command=converter_cm_m)
btn_converter.pack(pady=5)

# Exibir o resultado da conversão
label = tk.Label(janela, text="")
label.pack(pady=10)

janela.mainloop()
