import streamlit as st

class Livro:
    def __init__(self, titulo, autor, livro_id):
        self.titulo = titulo
        self.autor = autor
        self.livro_id = livro_id
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        return False

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"ID: {self.livro_id}, Título: {self.titulo}, Autor: {self.autor}, Status: {status}"


class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

    def emprestar_livro(self, livro):
        if livro.emprestar():
            self.historico_emprestimos.append(livro)
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.historico_emprestimos and livro.devolver():
            self.historico_emprestimos.remove(livro)
            return True
        return False

    def __str__(self):
        return f"Nome: {self.nome}, Número de Membro: {self.numero_membro}"


class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def emprestar_livro(self, livro_id, numero_membro):
        livro = self.buscar_livro_por_id(livro_id)
        membro = self.buscar_membro_por_numero(numero_membro)
        if livro and membro:
            if membro.emprestar_livro(livro):
                return f"Livro {livro.titulo} emprestado com sucesso a {membro.nome}."
            return "Livro já está emprestado."
        return "Livro ou Membro não encontrado."

    def devolver_livro(self, livro_id, numero_membro):
        livro = self.buscar_livro_por_id(livro_id)
        membro = self.buscar_membro_por_numero(numero_membro)
        if livro and membro:
            if membro.devolver_livro(livro):
                return f"Livro {livro.titulo} devolvido com sucesso por {membro.nome}."
            return "Livro não estava emprestado."
        return "Livro ou Membro não encontrado."

    def buscar_livro_por_id(self, livro_id):
        for livro in self.catalogo:
            if livro.livro_id == livro_id:
                return livro
        return None

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def buscar_livro_por_autor(self, autor):
        for livro in self.catalogo:
            if livro.autor.lower() == autor.lower():
                return livro
        return None

    def buscar_membro_por_numero(self, numero_membro):
        for membro in self.membros:
            if membro.numero_membro == numero_membro:
                return membro
        return None

    def exibir_catalogo(self):
        return "\n".join([str(livro) for livro in self.catalogo])

    def exibir_membros(self):
        return "\n".join([str(membro) for membro in self.membros])


# Instância da Biblioteca
biblioteca = Biblioteca()

# Interface Streamlit com Tabs
st.title("Sistema de Gerenciamento de Biblioteca")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Adicionar Livro", "Adicionar Membro", "Emprestar Livro", "Devolver Livro", "Buscar Livro", "Exibir Catálogo/Membros"])

with tab1:
    st.header("Adicionar Livro")
    titulo_livro = st.text_input("Título do Livro", key="titulo_livro")
    autor_livro = st.text_input("Autor do Livro", key="autor_livro")
    livro_id = st.text_input("ID do Livro", key="livro_id")
    if st.button("Adicionar Livro"):
        if titulo_livro and autor_livro and livro_id:
            novo_livro = Livro(titulo_livro, autor_livro, livro_id)
            biblioteca.adicionar_livro(novo_livro)
            st.success(f"Livro '{titulo_livro}' adicionado ao catálogo.")
        else:
            st.error("Por favor, preencha todos os campos.")

with tab2:
    st.header("Adicionar Membro")
    nome_membro = st.text_input("Nome do Membro", key="nome_membro")
    numero_membro = st.text_input("Número de Membro", key="numero_membro")
    if st.button("Adicionar Membro"):
        if nome_membro and numero_membro:
            novo_membro = Membro(nome_membro, numero_membro)
            biblioteca.adicionar_membro(novo_membro)
            st.success(f"Membro '{nome_membro}' adicionado à biblioteca.")
        else:
            st.error("Por favor, preencha todos os campos.")

with tab3:
    st.header("Emprestar Livro")
    emprestar_livro_id = st.text_input("ID do Livro para Emprestar", key="emprestar_livro_id")
    emprestar_numero_membro = st.text_input("Número do Membro", key="emprestar_numero_membro")
    if st.button("Emprestar Livro"):
        if emprestar_livro_id and emprestar_numero_membro:
            mensagem = biblioteca.emprestar_livro(emprestar_livro_id, emprestar_numero_membro)
            st.success(mensagem)
        else:
            st.error("Por favor, preencha todos os campos.")

with tab4:
    st.header("Devolver Livro")
    devolver_livro_id = st.text_input("ID do Livro para Devolver", key="devolver_livro_id")
    devolver_numero_membro = st.text_input("Número do Membro", key="devolver_numero_membro")
    if st.button("Devolver Livro"):
        if devolver_livro_id and devolver_numero_membro:
            mensagem = biblioteca.devolver_livro(devolver_livro_id, devolver_numero_membro)
            st.success(mensagem)
        else:
            st.error("Por favor, preencha todos os campos.")

with tab5:
    st.header("Buscar Livro")
    titulo_busca = st.text_input("Buscar Livro por Título", key="titulo_busca")
    autor_busca = st.text_input("Buscar Livro por Autor", key="autor_busca")
    livro_encontrado = None
    if st.button("Buscar Livro"):
        if titulo_busca:
            livro_encontrado = biblioteca.buscar_livro_por_titulo(titulo_busca)
        elif autor_busca:
            livro_encontrado = biblioteca.buscar_livro_por_autor(autor_busca)

        if livro_encontrado:
            st.success(f"Livro encontrado: {livro_encontrado}")
        else:
            st.error("Livro não encontrado.")

with tab6:
    st.header("Catálogo de Livros")
    if st.button("Exibir Catálogo"):
        catalogo = biblioteca.exibir_catalogo()
        if catalogo:
            st.text(catalogo)
        else:
            st.info("Nenhum livro no catálogo.")

    st.header("Membros da Biblioteca")
    if st.button("Exibir Membros"):
        membros = biblioteca.exibir_membros()
        if membros:
            st.text(membros)
        else:
            st.info("Nenhum membro registrado.")
