from classContaBancaria import ContaBancaria 
if (__name__ == "__main__"):
    conta = ContaBancaria("648583352" , "Marcos")

    conta.depositar(1000)
    conta.sacar(2000)
    conta.sacar(100)
    conta.exibirSaldo()
