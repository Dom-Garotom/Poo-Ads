from pessoa import Pessoa

class Aluno(Pessoa):
    _matric : str

    def __init__(self, nome, sexo , matricula):
        super().__init__(nome, sexo)
        self._matric = matricula