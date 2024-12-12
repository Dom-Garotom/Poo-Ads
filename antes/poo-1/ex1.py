class Pessoa :
    nome : str
    idade : 0
    peso : 0
    tamanho: 0.0

    def crescer (self, tamanho ) :
        if ( self.idade <= 21):
            self.tamanho += tamanho;
        else :
            print("Você não cresce mais como antes...")
    

    def engordar (self, peso):
        self.peso += peso
    
    def emagrecer (self, peso):
        self.peso -= peso

    def envelhecer (self, idade):
        self.idade += idade

        if ( self.idade <= 21 ):
            self.tamanho += (idade * 0.05)
    
    def mudarDeNome (self , nome):
        self.nome = nome

    def __init__(self , nome = "desconhecido" , idade = 0 , peso = 0 ,tamanho = 0.0 ):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tamanho = tamanho






