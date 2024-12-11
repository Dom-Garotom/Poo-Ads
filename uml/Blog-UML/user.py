import random

class User:
    id : int
    nome: str
    login: str
    senha: str

    def __init__(self , nome : str , login : str , senha : str):
        self._id =  random.randint(1 , 10000)    
        self.nome = nome 
        self.login =  login
        self.senha = senha
