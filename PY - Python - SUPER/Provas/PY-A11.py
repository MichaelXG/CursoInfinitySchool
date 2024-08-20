print("""
    PY-A11] Você foi contratado para desenvolver o software de controle de um elevador inteligente. 
    A classe Elevador foi criada para modelar esse sistema e possui os seguintes atributos: 
    totalCapacidade, atualCapacidade, totalAndar e atualAndar, que representam, respectivamente, 
    a capacidade máxima do elevador, a capacidade atual, o total de andares do prédio e o andar atual do elevador.

    A classe Elevador também possui os seguintes métodos:

    1. Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo".
       Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".
    2. Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo". 
       Caso contrário, exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".
    3. Entrar(): caso a capacidade atual do elevador não tenha sido atingida, o método incrementa o número de pessoas presentes no elevador 
       e exibe "Entrando uma pessoa". Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".
    4. Sair(): caso haja pelo menos uma pessoa no elevador, o método decrementa o número de pessoas presentes e exibe "Saindo uma pessoa". 
       Caso contrário, exibe "NÃO TEM NINGUÉM".
      """)

class Elevador:
    def __init__(self, total_capacidade, total_andar):
        self.total_capacidade = total_capacidade
        self.atual_capacidade = 0
        self.total_andar = total_andar
        self.atual_andar = 0  
    
    def subir(self):
        if self.atual_andar < self.total_andar:
            self.atual_andar += 1
            print("Subindo")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")
    
    def descer(self):
        if self.atual_andar > 0:
            self.atual_andar -= 1
            print("Descendo")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")
    
    def entrar(self):
        if self.atual_capacidade < self.total_capacidade:
            self.atual_capacidade += 1
            print("Entrando uma pessoa")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")
    
    def sair(self):
        if self.atual_capacidade > 0:
            self.atual_capacidade -= 1
            print("Saindo uma pessoa")
        else:
            print("NÃO TEM NINGUÉM")
            
            
elevador = Elevador(total_capacidade=8, total_andar=15)

 # Entrando 
elevador.entrar() 
 # Subindo
elevador.subir() 
 # Subindo 
elevador.subir()   
# Descendo
elevador.descer()  
# Saindo
elevador.sair()    

