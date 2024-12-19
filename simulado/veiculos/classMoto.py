from classVeiculos import Veiculos

class Moto(Veiculos):
    tipoGuidao : str

    def __init__(self, marca, modelo, ano , tipoGuidao : str):
        super().__init__(marca, modelo, ano)
        self.tipoGuidao = tipoGuidao

    def exibirDetalhes(self):
        super().exibirDetalhes()
        print("Tipo de guidao " , self.tipoGuidao )
