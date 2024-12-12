import datetime

class Contrato:
    _inicio : datetime.date
    _fim : datetime.date
    _salario : float

    def __init__(self ,  inicio : datetime.date , fim : datetime.date , salario : float):
        self._inicio = inicio
        self._fim = fim
        self._salario = salario