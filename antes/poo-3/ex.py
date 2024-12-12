class Categoria:
    def __init__ (self , nome):
        self.nome = nome
        self.desconto = 0.0

    def aplicar_desconto (self, porcentDesconto , preco : float):
        desconto = (porcentDesconto / 100) * preco
        precoFinal = preco - desconto

        return precoFinal


class Produto:
    nome : str
    preco : float
    estoque : int
    categoria : Categoria 

    def __init__(self ,  nome , preco : float , estoque , categoria : Categoria):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria 
        

    def adicionar_estoque(self , quantidade : int):
        self.estoque += quantidade

    def remover_estoque(self , quantidade):
        if (self.estoque > 0 ):
            self.estoque -= quantidade
        else:
            print("Infelizmente o estoque está zerado")
    
    def preco_com_desconto(self , desconto): 
        valorDoDesconto = self.categoria.aplicar_desconto(desconto , self.preco)
        return valorDoDesconto


class Pedido:
    carrinho : [Produto]
    quantidade : {}
    
    def __init__(self):
        self.carrinho = []
        self.quantidade = {}

    def adicionar_produto(self , produto : Produto , quantidade):
        self.carrinho.append(produto)
        produto.remover_estoque(quantidade)
        
        if produto.nome in self.quantidade:
            self.quantidade[produto.nome] += quantidade
        else :
            self.quantidade[produto.nome] = quantidade
    
    def remover_produto(self ,  produto : Produto):
        produto.adicionar_estoque(self.quantidade[produto.nome])
        self.carrinho.remove(produto)
        del self.quantidade[produto.nome]

    def  calcular_total(self):
        valor = 0 

        for produto in self.carrinho :

            if produto.nome in self.quantidade:

                produtoComDesconto = produto.preco_com_desconto(20)

                valor += ( produtoComDesconto * self.quantidade[produto.nome] ) 
        
        print("O seu pedido esta saindo no valor de R$ ", valor)

    
    def exibir_detalhes(self):
        print("Nota dos seus pedidos:\n")
        print("{:<15}{:<15}{:<10}".format("nome" , "quantidade" , "Valor com desconto"))

        for produto in self.carrinho :

            if produto.nome in self.quantidade:
                print("{:<20}{:<10}{:<10}".format(produto.nome , self.quantidade[produto.nome] , produto.preco_com_desconto(20)))
        
        self.calcular_total()




categoria_roupas = Categoria("Roupas")
categoria_eletrodomesticos = Categoria("Eletrodomésticos")

produto1 = Produto("Camiseta", 50.00, 10, categoria_roupas)
produto2 = Produto("Calca", 80.00, 5, categoria_roupas)
produto3 = Produto("Geladeira", 1200.00, 2, categoria_eletrodomesticos)


pedido = Pedido()
pedido.adicionar_produto(produto1, 2) 
pedido.adicionar_produto(produto2, 1)  
pedido.adicionar_produto(produto3, 1) 


pedido.exibir_detalhes()