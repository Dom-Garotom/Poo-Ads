from classCarro import Carro
from classMoto import Moto


if (__name__ == "__main__"):
    moto = Moto("yamaha" , "Fan" , "2022" , "solto")
    carro = Carro("Volks" , "Gol" , "2000" , "2")

    moto.exibirDetalhes() 
    print("\n")
    carro.exibirDetalhes()