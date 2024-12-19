from classListarOperacoes import ListaOperacoes

if (__name__ == "__main__"):
    operacao = ListaOperacoes()

    operacao.adicionar(4)
    operacao.adicionar(8)
    operacao.adicionar(5)

    print(operacao.lista[:])

    operacao.remover(4)
    operacao.remover(5)

    print(operacao.lista[:])


    