print("""
    [PY-A13] Classe Bomba de Combustível:

    Faça um programa completo utilizando classes e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

    i.tipoCombustivel.
    ii.valorLitro
    iii.quantidadeCombustivel

    Possua no mínimo esses métodos:

    i.abastecerPorValor( )
    método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada 
    no veículo
    
    ii.abastecerPorLitro( )
    método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    
    iii. alterarValor( )
    altera o valor do litro do combustível.
    
    iv. alterarCombustivel( )
    altera o tipo do combustível.
   
    v.  alterarQuantidadeCombustivel( )
    altera a quantidade de combustível restante na bomba.
    
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível 
    total na bomba
""")

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        quantidade_litros = valor / self.valor_litro
        if quantidade_litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= quantidade_litros
            print(f"Abastecido {quantidade_litros:.2f} litros de {self.tipo_combustivel}.")
        else:
            print("Quantidade de combustível na bomba insuficiente para abastecer esse valor.")
            print(f"Disponível: {self.quantidade_combustivel:.2f} litros.")

    def abastecer_por_litro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            print(f"Valor a ser pago pelo abastecimento de {litros:.2f} litros de {self.tipo_combustivel}: R$ {valor_a_pagar:.2f}.")
        else:
            print("Quantidade de combustível na bomba insuficiente para abastecer essa quantidade de litros.")
            print(f"Disponível: {self.quantidade_combustivel:.2f} litros.")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Valor por litro alterado para: R$ {self.valor_litro:.2f}.")

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
        print(f"Tipo de combustível alterado para: {self.tipo_combustivel}.")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível na bomba alterada para: {self.quantidade_combustivel:.2f} litros.")


# Criando uma instância da BombaCombustivel
bomba = BombaCombustivel(tipo_combustivel="Gasolina", valor_litro=6.49, quantidade_combustivel=1000)

# Abastecendo por valor
bomba.abastecer_por_valor(100)  # Abastecendo com R$100

# Abastecendo por litros
bomba.abastecer_por_litro(20)  # Abastecendo 20 litros

# Alterando o valor do litro
bomba.alterar_valor(6.99)

# Alterando o tipo de combustível
bomba.alterar_combustivel("Diesel")

# Alterando a quantidade de combustível na bomba
bomba.alterar_quantidade_combustivel(500)
