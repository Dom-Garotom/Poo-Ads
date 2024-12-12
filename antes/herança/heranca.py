import datetime

class ContaBancaria:
    titular: str
    numero_conta: str
    saldo: float

    def __init__(self , titular: str , numeroBancario):
        self.titular = titular
        self.numero_conta = numeroBancario
        self.saldo = 0.0

    def deposito(self, valor: float):
        self.saldo += valor
    
    def sacar(self , valor: float):
        if (self.saldo >= valor):
            self.saldo -= valor
            return
    
        print("Saldo insuficiente")

    def exibir_saldo(self):
        print("Saldo atual na sua conta: " , self.saldo)
    

class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        taxa = 0.02
        limite = 1000

        if ( valor <  self.saldo):
            return super().sacar(valor * taxa)
        
        if (valor > self.saldo + limite ):
            print("Seu limite de credito é 1000, você ultrapacou o seu limite de crédito")
            return 
        
        return super().sacar( (valor + limite) * taxa )

class ContaPoupanca(ContaBancaria):
    def aplicar_rendimento(self , taxa : float):
        self.saldo = self.saldo * taxa

class ContaSalario(ContaBancaria):
    saques : int
    currentMonth : int

    def __init__(self, titular, numeroBancario):
        self.saques = 0
        self.currentMonth = datetime.date.today().month
        super().__init__(titular, numeroBancario)


    def sacar(self, valor):
        
        
        if (self.currentMonth < datetime.date.today().month):
            self.currentMonth = datetime.date.today().month
            self.saques = 0


        if( self.saques >= 1):
            print("Voce exedeu o limite de saques permitidos durante esse mes!")
            return

        self.saques += 1 
        
        return super().sacar(valor)  


def testar_contas():
    
    conta_corrente = ContaCorrente("Alice", "001")
    conta_poupanca = ContaPoupanca("Bob", "002")
    conta_salario = ContaSalario("Charlie", "003")

 
    conta_corrente.deposito(1500)
    conta_poupanca.deposito(2000)
    conta_salario.deposito(1200)

  
    conta_corrente.sacar(500) 
    conta_corrente.sacar(2000)  

    conta_poupanca.sacar(300)  
    conta_poupanca.aplicar_rendimento(0.05)  

    conta_salario.sacar(200) 
    conta_salario.sacar(100)  # deve falhar

  
    conta_corrente.exibir_saldo()
    conta_poupanca.exibir_saldo()
    conta_salario.exibir_saldo()

testar_contas()
