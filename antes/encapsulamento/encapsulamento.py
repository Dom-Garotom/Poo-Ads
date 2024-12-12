import uuid

class Livro:

    def __init__(self , titulo : str , autor : str , ano_publicacao : int , isbn : str , disponivel : bool   ):
        self.titulo = titulo;
        self.autor = autor;
        self.ano_publicacao = ano_publicacao;
        self.__isbn = isbn;
        self.__disponivel = disponivel;


    def get_isbn(self):
        return self.__isbn;

    def set_isbn(self , novo_isbn : str):
        if ( novo_isbn.len() > 13):
            self.__isbn = novo_isbn;
    def emprestar(self):
        if (self.__disponivel):
            self.__disponivel = False;

    def devolver(self):
        self.__disponivel = True

    def exibir_informacoes(self):
        print("{:<10} {:<10} {:<10} {:<10}".format(self.titulo, self.autor , self.ano_publicacao , self.__disponivel))

    
class Autor:
    nome: str
    __data_nascimento: int    
    nacionalidade: str

    def __init__(self, nome : str, data_nascimento : int, nacionalidade : str):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.__data_nascimento = data_nascimento

    def get_data_nascimento(self):
        return self.__data_nascimento
    
    def set_data_nascimento(self, nova_data):
        self.__data_nascimento = nova_data
    
    def exibir_informacoes(self): 
        print("{:<10} {:<10} {:<10}".format(self.nome , self.__data_nascimento , self.nacionalidade))
        
    
class Usuario:
    nome: str
    endereco : str
    telefone: str
    __id_usuario : int
    __livros_emprestados: list

    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.__id_usuario = uuid.uuid4()
        self.__livros_emprestados = []
    
    def get_id_usuario(self):
        return self.__id_usuario
    
    def emprestar_livro(self, livro : Livro):
        self.__livros_emprestados.append(livro)

    def devolver_livro(self, livro : Livro):
        if (livro in self.__livros_emprestados):
            self.__livros_emprestados.remove(livro)
    
    def exibir_informacoes(self): 
        print("{:<10} \n{:<10} \n{:<10} ".format(self.nome , self.endereco, self.telefone))

        if self.__livros_emprestados :
            print('Livros emprestados :' )
            for livro in self.__livros_emprestados:
                print(livro.titulo)
        print("")

        
livros = []
autores = []
usuarios = []


def cadastrar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    ano_publicacao = int(input("Ano de publicação: "))
    isbn = input("ISBN: ")
    disponivel = True
    novo_livro = Livro(titulo, autor, ano_publicacao, isbn, disponivel)
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso.")


def cadastrar_autor():
    nome = input("Nome do autor: ")
    data_nascimento = int(input("Ano de nascimento: "))
    nacionalidade = input("Nacionalidade: ")
    novo_autor = Autor(nome, data_nascimento, nacionalidade)
    autores.append(novo_autor)
    print("Autor cadastrado com sucesso.")


def cadastrar_usuario():
    nome = input("Nome do usuário: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    novo_usuario = Usuario(nome, endereco, telefone)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")


def emprestar_livro():
    nome_usuario = input("Nome do usuário: ")
    titulo_livro = input("Título do livro para empréstimo: ")

    usuario = next((u for u in usuarios if u.nome == nome_usuario), None)
    livro = next((l for l in livros if l.titulo == titulo_livro), None)

    if usuario and livro:
        usuario.emprestar_livro(livro)
    else:
        print("Usuário ou livro não encontrado.")


def devolver_livro():
    nome_usuario = input("Nome do usuário: ")
    titulo_livro = input("Título do livro para devolução: ")

    usuario = next((u for u in usuarios if u.nome == nome_usuario), None)
    livro = next((l for l in livros if l.titulo == titulo_livro), None)

    if usuario and livro:
        usuario.devolver_livro(livro)
    else:
        print("Usuário ou livro não encontrado.")


def exibir_livros():
    print("Lista de livros cadastrados:")
    for livro in livros:
        livro.exibir_informacoes()


def exibir_autores():
    print("Lista de autores cadastrados:")
    for autor in autores:
        autor.exibir_informacoes()


def exibir_usuarios():
    print("Lista de usuários cadastrados:")
    for usuario in usuarios:
        usuario.exibir_informacoes()


def pesquisar_livro():
    criterio = input("Pesquisar por título (T), autor (A) ou ISBN (I): ").strip().upper()
    termo = input("Informe o termo de pesquisa: ")

    if criterio == 'T':
        resultado = [l for l in livros if termo.lower() in l.titulo.lower()]
    elif criterio == 'A':
        resultado = [l for l in livros if termo.lower() in l.autor.lower()]
    elif criterio == 'I':
        resultado = [l for l in livros if termo == l.get_isbn()]
    else:
        print("Critério inválido.")
        return

    print("Resultado da pesquisa:")
    for livro in resultado:
        livro.exibir_informacoes()


def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Autor")
        print("3. Cadastrar Usuário")
        print("4. Emprestar Livro")
        print("5. Devolver Livro")
        print("6. Exibir Livros")
        print("7. Exibir Autores")
        print("8. Exibir Usuários")
        print("9. Pesquisar Livro")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            cadastrar_autor()
        elif opcao == '3':
            cadastrar_usuario()
        elif opcao == '4':
            emprestar_livro()
        elif opcao == '5':
            devolver_livro()
        elif opcao == '6':
            exibir_livros()
        elif opcao == '7':
            exibir_autores()
        elif opcao == '8':
            exibir_usuarios()
        elif opcao == '9':
            pesquisar_livro()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()