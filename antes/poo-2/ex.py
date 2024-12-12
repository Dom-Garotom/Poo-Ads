class CarroDeCorrida:
    marca: str
    modelo: str
    velocidade_atual: float 
    velocidade_maxima: float 
    capacidade_maxima_tanque_combustivel : float
    tanque_combustivel: float 
    consumo_combustivel: float
    posicao : float

    def __init__(self, modelo, marca , capacidadeMaxima , consumo , velocidadeMaxima):
        self.modelo = modelo
        self.marca = marca
        self.capacidade_maxima_tanque_combustivel = capacidadeMaxima
        self.tanque_combustivel = capacidadeMaxima
        self.consumo_combustivel = consumo
        self.velocidade_maxima = velocidadeMaxima
        self.velocidade_atual = 0
        self.posicao = 4


    def acelerar( self , quantidade: float):

        if(self.tanque_combustivel == 0 ):
            print("O carro está sem gasolina")
            return

        if (self.velocidade_atual == self.velocidade_maxima):
            print("O carro está na su capacidade máxima a ", self.velocidade_maxima , "km/h")
        else:
            self.velocidade_atual += quantidade
            print("O carro está acelerando para ", self.velocidade_atual ,"km/h")


    def frear(self , quantidade: float): 
        if (self.velocidade_atual == 0):
            print("Seu carro está parado!")
        else:
            self.velocidade_atual-= quantidade
            print("Diminuindo para " , self.velocidade_atual , "km/h")


    def abastecer( self , litros: float):
        if (self.tanque_combustivel== self.capacidade_maxima_tanque_combustivel):
            print("Seu tanque está cheio")
        else:
            self.tanque_combustivel += litros
            print("Abatecendo o tanque.... Capacidade: " , self.tanque_combustivel , "litros")

    
    def dirigir( self  , distancia: float):
        tanqueAtual = self.tanque_combustivel
        self.tanque_combustivel -=  (distancia * self.consumo_combustivel)

        if ( self.tanque_combustivel == 0 ):
            print("A sua gasolina acabou")
    
    def verificar_combustivel(self): 
        return self.tanque_combustivel

    def subirPosicao (self):
        if (self.posicao >= 2 ):
            self.posicao -= 1

    def status(self): 
        print(
            "Modelo : "  , self.modelo,
            "Marca : "  , self.marca,
            "Velocidade atual : "  , self.velocidade_atual,
            "Velocidade máxima : "  , self.velocidade_maxima,
            "Tanque : "  , self.tanque_combustivel,
            "Capacidade máxima do tanque : "  , self.capacidade_maxima_tanque_combustivel,
            "Nível de consumo por kmh : "  , self.consumo_combustivel,
        )

        


class Corrida:
    carros : []
    distancia_total: float
    vencedor: str

    def __init__(self):
        self.carros = []
        self.vencedor = ''


    def adicionar_carro(self , carro: CarroDeCorrida):
        self.carros.append(carro)

    def iniciar_corrida(self , distancia):
        self.distancia_total = distancia 
        concluintes = []

        for carro in self.carros:
            carro.dirigir(self.distancia_total)

            if ( carro.verificar_combustivel != 0):
                concluintes.append(carro)
        
        for carro in concluintes:
            for i in range(len(concluintes)):
                if (carro.velocidade_atual > concluintes[i].velocidade_atual):
                    carro.subirPosicao()

        menorPosicao = len(self.carros)

        for carro in concluintes:
            if ( carro.posicao < menorPosicao):
                menorPosicao =  carro.posicao

        for carro in concluintes:
            if (carro.posicao == menorPosicao):
                self.vencedor = carro.modelo
        
    def resultado_corrida(self):
        print("O grande vencedor da corrida e :" , self.vencedor) 

GrandPri = Corrida()

vestapen = CarroDeCorrida("M40-2","Mercedes", 150.0 , 0.08 , 300 )
Hemilton = CarroDeCorrida("M1-03","McLare", 150.0 , 0.08 , 300)
FelipeMassa = CarroDeCorrida("F3-44","Ferrari", 150.0 , 0.06 , 300)
Massa = CarroDeCorrida("F44","Ferrari", 50.0 , 0.08 , 300)

vestapen.acelerar(290.0)
Hemilton.acelerar(290.0)
FelipeMassa.acelerar(290.5)
Massa.acelerar(280.5)


GrandPri.adicionar_carro(vestapen)
GrandPri.adicionar_carro(FelipeMassa)
GrandPri.adicionar_carro(Massa)
GrandPri.adicionar_carro(Hemilton)

GrandPri.iniciar_corrida(100.0)
GrandPri.resultado_corrida()