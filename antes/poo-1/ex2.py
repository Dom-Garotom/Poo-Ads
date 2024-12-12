class Conta:

    def __init__ (self ,  numero , titular , saldo ,  limite , codigo_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo = codigo_tipo

        if (codigo_tipo == "01"):
            self.nome_tipo = "conta corrente"
        elif ( codigo_tipo == "02"):
            self.nome_tipo = "poupança"

    
    def transferencia (self , valor , destino):
        self.saldo -= valor
        print("Valor :" , valor , " foi enviado para a conta :" , destino)

    
    def depositar(self , valor):
        self.saldo += valor
    
    def sacar(self , valor):
        if (self.saldo != 0):
            self.saldo -= valor
            return True
        else:
            return False

    def extrato(self ):
        print("Numero: {} \nSaldo: {}".format( self.numero , self.saldo))


conta1 = Conta('00.002' , "Marcos Aurelio" , 124343.00 , 1725443.00 , "01")


numero = input("Numero da conta: ")
titular = input("Titular da conta: ")
saldo = float(input("Saldo da conta: "))
limite = float(input("Limite da conta: "))
codigo_tipo=input("Codigo do tipo da conta: ")


conta2 = Conta(numero, titular , saldo , limite , codigo_tipo );

valor = float(input("Qual o valor que você deseja tranferir: "))
destino = input("Qual o numero da conta que você deseja transferir: ")

conta2.transferencia(valor , destino)
conta2.extrato()

