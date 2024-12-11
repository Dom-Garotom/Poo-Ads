from itemPedido import ItemPedido

class Pedido : 
    __valor_total : float

    def __init__(self):
        self.__valor_total = 0

    def adicionar_item(self , itemPedido : ItemPedido) :
        self.__valor_total += itemPedido._quantidade * itemPedido.produto._valor

    def obter_total (self):
        return self.__valor_total