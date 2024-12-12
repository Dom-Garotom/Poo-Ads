class Produto:
    nome: str
    preco: float
    quantidade_em_estoque:int

    def __init__(self, nome : str, preco : float, quantidade_em_estoque : int):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def vender(self, quantidade : int):
        self.quantidade_em_estoque -= quantidade
    
    def repor_estoque(self, quantidade : int):
        self.quantidade_em_estoque += quantidade

    def exibir_informacoes(self):
        print("{:<20}  {:<10}  {:<10}  {:<10}".format("nome" , "preco" , "quantidade em estoque"))
        print("{:<20}  {:<10}  {:<10}  {:<10}".format(self.nome , self.preco , self.quantidade_em_estoque))

    
class Racao(Produto):
    tipo_animal : str
    peso: float

    def __init__(self, nome, preco, quantidade_em_estoque , tipo , peso):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.tipo_animal = tipo
        self.peso = peso

class Brinquedo(Produto):
    material: str
    faixa_etaria: str

    def __init__(self, nome, preco, quantidade_em_estoque , meterial , etaria):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.material = meterial
        self.faixa_etaria = etaria

class Medicamento(Produto):
    tipo: str
    dosagem: str

    def __init__(self, nome, preco, quantidade_em_estoque , tipo , dosagem):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.tipo = tipo
        self.dosagem = dosagem

class Acessorio(Produto):
    categoria: str
    tamanho :  str

    def __init__(self, nome, preco, quantidade_em_estoque , categoria , tamanho):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.categoria = categoria
        self.tamanho = tamanho



class Menu :
    produtos : []
    mais_vendido : str
    quantidade_de_vendas: int 

    def __init__(self):
        self.produtos = []
        self.mais_vendido = ""
        self.quantidade_de_vendas = 0 

    def registrar_produto (self , produto : Produto):
        self.produtos.append(produto)
    
    def consultar_produto (self, produto):
        if (produto in self.produtos):

            for produtos in self.produtos:
                if ( produtos == produto):
                    print("Esse produto tem " , produtos.quantidade_em_estoque , " itens em estoque")
                    if(produto.quantidade_em_estoque <= 5):
                        print("Considere repor o estoque porque ele esta perto de acabar")
            
            return

        print("O produto informado não foi cadastrado no sistema")  

    def vender(self , item , quantidade_Vendida : int):
        if (item in self.produtos):
            for produtos in self.produtos:
                if ( produtos == item):
                    item.vender(quantidade_Vendida)

            if (item.nome != self.mais_vendido and quantidade_Vendida > self.quantidade_de_vendas):
                self.mais_vendido = item.nome
                self.quantidade_de_vendas = quantidade_Vendida
                return
            
            if (item.nome == self.mais_vendido):
                self.quantidade_de_vendas += quantidade_Vendida
                return

            return

        print("O produto informado não foi cadastrado no sistema") 

    def repor(self , item , quantidade):
        if (item in self.produtos):
            for produtos in self.produtos:
                if ( produtos == item):
                    item.repor_estoque(quantidade)
            return

        print("O produto informado não foi cadastrado no sistema")

    def relatorio(self):
        print("\nO produto com mais vendas no sistema:\n")
        print("{:<20} {:<10}".format("Nome" , "Quantidade"))
        print("{:<20} {:<10}".format(self.mais_vendido , self.quantidade_de_vendas))


def criar_produto (nome , preco , quantidade , tipo_de_produto): 
    parametro1 = ''
    parametro2 = ''

    match tipo_de_produto:
        case "racao":
            parametro1 = input("Qual o tipo de animal")
            parametro2 = float(input("Peso da racao"))
            return Racao(nome, preco , quantidade , parametro1 , parametro2)
        case "brinquedo":
            parametro1 = input("Qual o materia do brinquedo")
            parametro2 = input("Qual a faixa etaria do brinquedo")
            return Brinquedo(nome, preco , quantidade , parametro1 , parametro2)
        case "medicamento":
            parametro1 = input("Qual o tipo do medicamento")
            parametro2 = input("Qual a dosagem necessaria")
            return Medicamento(nome, preco , quantidade , parametro1 , parametro2)
        case "acessorio":
            parametro1 = input("Qual a categoria do produto")
            parametro2 = input("Qual o tamanho do produto")
            return Acessorio(nome, preco , quantidade , parametro1 , parametro2)

menu = Menu()

while True:
    acao = int(input("O que você gostaria de fazer?\n"
                     "1 - Cadastrar um produto\n"
                     "2 - Consultar estoque de um produto\n"
                     "3 - Vender um produto\n"
                     "4 - Repor um produto\n"
                     "5 - Exibir relatório\n"
                     "6 - Sair\n"))

    match acao:
        case 1:
            tipo_produto = input("Qual o tipo do produto? (racao, brinquedo, medicamento, acessorio): ").lower()
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade em estoque: "))
            produto = criar_produto(nome, preco, quantidade, tipo_produto)
            if produto:
                menu.registrar_produto(produto)
                print("Produto cadastrado com sucesso.")
        case 2:
            nome_produto = input("Nome do produto para consulta: ")
            produto = next((p for p in menu.produtos if p.nome == nome_produto), None)
            if produto:
                menu.consultar_produto(produto)
            else:
                print("Produto não encontrado.")

        case 3:
            nome_produto = input("Nome do produto para venda: ")
            quantidade_venda = int(input("Quantidade a ser vendida: "))
            produto = next((p for p in menu.produtos if p.nome == nome_produto), None)
            if produto:
                menu.vender(produto, quantidade_venda)
                print("Venda realizada.")
            else:
                print("Produto não encontrado.")

        case 4:
            nome_produto = input("Nome do produto para repor: ")
            quantidade_repor = int(input("Quantidade a ser reposta: "))
            produto = next((p for p in menu.produtos if p.nome == nome_produto), None)
            if produto:
                menu.repor(produto, quantidade_repor)
                print("Reposição realizada.")
            else:
                print("Produto não encontrado.")

        case 5:
            menu.relatorio()

        case 6:
            print("Saindo do sistema.")
            break

























racao = Racao("Racao para gatos" , 10.90 , 10)
brinquedo = Brinquedo("MaxSteel" , 5.99 , 100)
dipirona = Medicamento("dipirona" , 10.90 , 50)
relogio = Acessorio("rolex" , 1000.99 , 5)

menu.registrar_produto(racao)
menu.registrar_produto(brinquedo)
menu.registrar_produto(dipirona)
menu.registrar_produto(relogio)


menu.vender(racao, 10)
menu.repor(racao , 2)

menu.consultar_produto(racao)
menu.relatorio()