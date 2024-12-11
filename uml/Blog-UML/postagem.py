import datetime
import random

class Postagem : 
    _id: int
    _titulo: str
    _texto: str
    _dataPublicacao: datetime

    def __init__(self , titulo : str , texto : str , ano : int , mes : int , dia : int):
        self._id =  random.randint(1 , 10000)       
        self._titulo = titulo
        self._texto = texto
        self._dataPublicacao = datetime.datetime( ano  , mes , dia)