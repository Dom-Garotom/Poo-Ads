import abc





class Alugavel:
    __mobiliado:str
    __preco:float

    def __init__(self ,  mobiliado : bool , preco : float):
        self.__preco = preco
        
        if (mobiliado == True):
            self.__mobiliado = "e mobiliado"
        else:
            self.__mobiliado = "nao e mobiliado"
    
    def getPreco(self):
        return self.__preco

    def setPreco(self , preco:float):
        self.__preco = preco
    
    def getMobiliado(self):
        return self.__mobiliado
    
    def setMobiliado(self , mobiliado : bool):
        if (mobiliado == True):
            self.__mobiliado = "e mobiliado"
        else:
            self.__mobiliado = "nao e mobiliado"
    
    def alugar (self , nome : str):
        print("alugado pelo valor de R${} para {}".format(self.__preco , nome))

    def __str__(self):
        info = "\nmobiliado : {} \npreco : {}".format(self.__mobiliado , self.__preco)
        return info
    


class Compravel:
    __preco:float
    __taxas:float

    def __init__(self ,  taxa : float , preco : float):
        self.__taxas = taxa
        self.__preco = preco
    
    def getTaxa(self):
        return self.__taxas

    def setTaxa(self , taxa:float):
        self.__taxas = taxa
    
    def getPreco(self):
        return self.__preco
    
    def setPreco(self , preco : float):
        self.__preco = preco




    
    def realizar_compra(self , nome : str):
        print("comprado pelo valor de  R${} para o comprador {}".format(self.__preco , nome))

    def __str__(self):
        info = "\npreco : {} \ntaxa : {}".format(self.__preco , self.__taxas)
        return info
        



class Propriedade:
    __espaco_construido : int
    __num_quartos: int 
    __num_banheiros: int 


    def __init__(self ,  espaco , quartos , banheiros ):
        self.__espaco_construido = espaco
        self.__num_quartos = quartos
        self.__num_banheiros = banheiros


    def  indice_aproveitamento(self):
        abc.abstractmethod(self)
    

    def getEspaco_construido (self):
        return self.__espaco_construido
    
    def setEspaco_construido (self , espaco):
        self.__espaco_construido = espaco


    def getNum_quartos (self):
        return self.__num_quartos
    
    def setNum_quartos (self , quartos):
        self.__num_quartos = quartos



    def getNum_banheiros (self):
        return self.__num_banheiros
    
    def setNum_banheiros (self , banheiros):
        self.__num_banheiros = banheiros    
    

    def display (self):
        print(self)

    def __str__(self):
        abc.abstractmethod(self)

    




class Apartamento (Propriedade , Alugavel , Compravel):
    __varanda : str
    __andar : int

    def __init__(self, espaco, quartos, banheiros , varanda : bool , andar : int , alugado : bool , precoAlugar : float , taxa : float , compra : float):
        super().__init__( espaco, quartos, banheiros)
        Alugavel.__init__(self , alugado , precoAlugar)
        Compravel.__init__(self , taxa , compra)

        self.__andar = andar
        
        if (varanda == True):
            self.__varanda = "possui varanda"
        else:
            self.__varanda = "nao possui varanda"

    def indice_aproveitamento(self):
        indice =  ( self.getNum_banheiros() + self.getNum_quartos() ) / self.getEspaco_construido() 
        print("Indice de aproveitamento : {}".format(indice))

    def getVaranda(self):
        return self.__varanda
    
    def setVaranda (self , varanda : bool):
        if (varanda == True):
            self.__varanda = "possui varanda"
        else:
            self.__varanda = "nao possui varanda"
    
    def getAndar(self):
        return self.__andar
    
    def setAndar(self , andar : int ):
        self.__andar = andar

    def __str__(self):
        infoSuper = "espaco_construido : {} \nnum_quartos: {}  \nnum_banheiros : {}".format(
            self.getEspaco_construido() , 
            self.getNum_quartos() , 
            self.getNum_banheiros() 
        )

        info = infoSuper +  "\nvaranda: {} \nAndar : {}".format(self.__varanda , self.__andar)
        return info

    def display(self):
        super().display()

        info = "Preco de compra: {} \nTaxa : {}\nMobiliado: {}\nAluguel : {}".format(
            Compravel.getPreco(self),
            self.getTaxa(),
            self.getMobiliado(),
            self.getPreco(),
            self.indice_aproveitamento()
        )

        print(info)
        self.indice_aproveitamento()





class Casa(Propriedade , Alugavel , Compravel):
    __garagem : str 
    __quintal : str

    def __init__(self, espaco, quartos, banheiros , garagem : bool , quintal : bool, alugado : bool , precoAlugar : float , taxa : float , compra : float):
        super().__init__(espaco, quartos, banheiros)
        Alugavel.__init__(self , alugado , precoAlugar)
        Compravel.__init__(self , taxa , compra)

        if (quintal == True):
            self.__quintal = "possui quinta"
        else:
            self.__quintal = "nao possui quintal"
        
        if (garagem == True):
            self.__garagem = "possui garagem"
        else:
            self.__garagem = "nao possui garagem"

    def indice_aproveitamento(self):
        indice =  ( self.getNum_banheiros() + self.getNum_quartos() ) / self.getEspaco_construido() 
        print("Indice de aproveitamento : {}".format(indice))

    def getGaragem(self):
        return self.__garagem


    def setGaragem (self , garagem : bool):
        if (garagem == True):
            self.__garagem = "possui garagem"
        else:
            self.__garagem = "nao possui garagem"
    
    def getQuintal (self):
        return self.__quintal
    
    def setQuintal(self , quintal : bool):
        if (quintal == True):
            self.__quintal = "possui quinta"
        else:
            self.__quintal = "nao possui quintal"
    
    def __str__(self):
        infoSuper = "espaco_construido : {} \nnum_quartos: {}  \nnum_banheiros : {}".format(
            self.getEspaco_construido() , 
            self.getNum_quartos() , 
            self.getNum_banheiros() 
        )


        info = infoSuper+  "\nquintal: {} \ngaragem : {}".format(self.__quintal , self.__garagem)
        return info

    def display(self):
        super().display()

        info = "Preco de compra: {} \nTaxa : {}\nMobiliado: {}\nAluguel : {}".format(
            Compravel.getPreco(self),
            self.getTaxa(),
            self.getMobiliado(),
            self.getPreco(),
        )

        print(info)
        self.indice_aproveitamento()



class Hotel(Propriedade ,  Compravel):
    __andares : int
    __elevador: str


    def __init__(self, espaco, quartos, banheiros , andares : int , elevador : bool , taxa : float , preco : float):
        super().__init__(espaco, quartos, banheiros)
        Compravel.__init__(self , taxa , preco)

        self.__andares = andares

        if (elevador == True):
            self.__elevador = "possui elevador"
        else:
            self.__elevador = "nao possui elevador"
    
    
    def indice_aproveitamento(self):
        indice =  ( self.getNum_banheiros() + self.getNum_quartos() ) / self.getEspaco_construido() 
        indice = indice * self.__andares - 1
        print("Indice de aproveitamento : {}".format(indice))
    

    def getAndares(self):
        return self.__andares


    def setAndares (self , andares : int):
        self.__andares = andares
    


    def getElevador (self):
        return self.__elevador
    
    def setElevador(self , elevador : bool):
        if (elevador == True):
            self.__elevador = "possui elevador"
        else:
            self.__elevador = "nao possui elevador"
    
    def __str__(self):
        infoSuper = "espaco_construido : {} \nnum_quartos: {}  \nnum_banheiros : {}".format(
            self.getEspaco_construido() , 
            self.getNum_quartos() , 
            self.getNum_banheiros() 
        )

        info = infoSuper +  "\nelevador: {} \nandares : {}".format(self.__elevador , self.__andares)
        return info

    def display(self):
        super().display()

        info = "Preco de compra: {} \nTaxa : {}".format(
            self.getPreco(),
            self.getTaxa(),
            self.indice_aproveitamento()
        )

        print(info)
        self.indice_aproveitamento()




