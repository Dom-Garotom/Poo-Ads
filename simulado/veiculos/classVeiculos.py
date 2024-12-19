class Veiculos:
    marca : str
    modelo : str 
    ano : str

    def __init__(self , marca : str , modelo : str , ano : str):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano

    def exibirDetalhes( self ):
        print("Marca {} \nModelo {} \nAno {}".format(self.marca , self.modelo , self.ano))