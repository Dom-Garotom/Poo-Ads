class ContaBancaria:
    numeroConta : str
    titular : str
    saldo : float

    def __init__(self , numeroConta : str  ,  titular : str):
        self.numeroConta = numeroConta
        self.titular = titular
        self.saldo = 0.0
        


    def depositar(self , valor: float):
        self.saldo += valor

    def sacar( self , valor: float):
        if (valor > self.saldo):
            print("Saldo insuficiente")
            return
        
        self.saldo -= valor
    
    def exibirSaldo( self ):
        print("Seu saldo atual :" , self.saldo)
