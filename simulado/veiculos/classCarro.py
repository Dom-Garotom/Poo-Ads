from classVeiculos import Veiculos

class Carro(Veiculos):
    numPortas : int

    def __init__(self, marca, modelo, ano , numPortas):
        super().__init__(marca, modelo, ano)
        self.numPortas = numPortas

    def exibirDetalhes(self):
        super().exibirDetalhes()
        print("Numero de portas " , self.numPortas)