import datetime

class Pessoa:
    _nome : str
    _sexo : str
    _data_nasc : datetime.datetime

    def __init__(self ,  nome : str , sexo : str):
        self._nome = nome
        self._sexo = sexo
        self._data_nasc = datetime.datetime.now()