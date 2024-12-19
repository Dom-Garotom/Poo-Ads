from interface import Interface

class ListaOperacoes(Interface):
    lista : list

    def __init__(self):
        self.lista = []

    def adicionar(self , valor : int):
        self.lista.append(valor)
    
    def remover(self , valor : int):
        self.lista.remove(valor)
               
            

    
