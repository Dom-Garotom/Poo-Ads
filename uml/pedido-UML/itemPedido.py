from produto import Produto 

class ItemPedido:
    _quantidade : int

    def __init__(self , produto : Produto , quantidade : int):
        self._quantidade = quantidade
        self.produto = produto

        
# quetionar o professor como se deve fazer a passagem do valor do produto para o pedido só usando a propriedade de quantidade apeas seguindo a uml 