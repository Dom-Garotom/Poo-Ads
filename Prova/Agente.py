from Property import Propriedade

class Agente :
    __lista : list[Propriedade]

    def __init__(self):
        self.__lista = []
    
    def display_propriedades(self):
        for prop in self.__lista:
            prop.display()
            print("\n" + "-"*125 + "\n") 

    
    def adicionar_propriedade( self , propriedade):
        self.__lista.append(propriedade)
    
    def remover_propriedade(self , propriedade):
        self.__lista.remove(propriedade)
    
    def get_lista_de_propriedades(self):
        return self.__lista
    
    def status_do_imovel(self , propriedade):
        return propriedade.__class__.__bases__