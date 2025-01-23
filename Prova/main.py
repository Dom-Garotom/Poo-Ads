from Property import Propriedade
from Property import Apartamento
from Property import Hotel
from Property import Casa
from Agente import Agente



if ( __name__ == "__main__"):
    propriedade = Propriedade(10 , 10 , 10)
    apartamento = Apartamento(10 , 10 , 10, True , 5 , True , 200.00 , 100.00 , 15000.00)
    casa = Casa(10 , 10 , 10, True , True , False , 0.00 , 500.00 , 15000.00)
    hotel = Hotel(10 , 10 , 10, 5 , True , 1000.00 , 100000.00)


    agente = Agente()

    agente.adicionar_propriedade(apartamento)
    agente.adicionar_propriedade(casa)
    agente.adicionar_propriedade(hotel)

    print("Executando a lista de display\n")

    agente.display_propriedades()

    print("removendo a casa\n")

    agente.remover_propriedade(casa)

    print("Executando a lista de display sem a casa\n")

    agente.display_propriedades()



    print("Lista de propriedades \n")
    lista = agente.get_lista_de_propriedades()
    print(lista)




    print("\n\nLista de classes pais de Casa \n")
    lista2 = agente.status_do_imovel(casa)
    print(lista2)

    print("\n" + "-"*125 + "\n") 


    