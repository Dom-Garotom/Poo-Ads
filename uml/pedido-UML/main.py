from produto import Produto
from itemPedido import ItemPedido
from pedido import Pedido

produto1 = Produto(1, 100.0, "Smartphone")
produto2 = Produto(2, 50.0, "Fone de Ouvido")
produto3 = Produto(3, 30.0, "Carregador USB")

item1 = ItemPedido(produto1, 2)  
item2 = ItemPedido(produto2, 1)  
item3 = ItemPedido(produto3, 3) 

pedido1 = Pedido()

pedido1.adicionar_item(item1)
pedido1.adicionar_item(item2)
pedido1.adicionar_item(item3)

print("Detalhes do Pedido:")

print("Valor Total do Pedido:", pedido1.obter_total())
