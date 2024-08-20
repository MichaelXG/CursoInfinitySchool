print("""
    [PY-A12]  Crie um código em Python que contenha as seguintes classes:
        
    A classe principal será chamada de "Material" e terá um construtor que recebe dois parâmetros: 
    "titulo" e "autor_ou_editora". 
    Essa classe também terá um método chamado "exibir_informacoes" que imprimirá na saída o título 
    e o autor/editora do material.

     A classe "Livro" será uma subclasse da classe "Material" e terá um construtor que recebe três 
    parâmetros: "titulo", "autor_ou_editora" e "genero". Essa classe também terá um método 
    "exibir_informacoes" que chamará o método correspondente na classe "Material" e imprimirá 
    o gênero do livro.

    A classe "Revista" será outra subclasse da classe "Material" e terá um construtor que recebe três 
    parâmetros: "titulo", "autor_ou_editora" e "edicao". Essa classe também terá um método 
    "exibir_informacoes" que chamará o método correspondente na classe "Material" e imprimirá a 
    edição da revista.

    Crie instâncias das classes "Livro" e "Revista" com informações específicas e chame o método 
    "exibir_informacoes" para mostrar os detalhes de cada material.
""")

# Classe principal Material
class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor/Editora: {self.autor_ou_editora}")

# Subclasse Livro
class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Gênero: {self.genero}")

# Subclasse Revista
class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Edição: {self.edicao}")

# Criando instâncias das classes Livro e Revista
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
revista1 = Revista("National Geographic", "NatGeo", "Edição 2024")

# Exibindo as informações
livro1.exibir_informacoes()
print()  # Apenas para separar as saídas
revista1.exibir_informacoes()

