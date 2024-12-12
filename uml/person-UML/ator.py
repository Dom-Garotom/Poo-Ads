from pessoa import Pessoa
from contrato import Contrato

class Ator (Pessoa):
    _contrato : Contrato

    def __init__(self, nome : str , sexo : str , contrato : Contrato):
        super().__init__(nome, sexo)
        self._contrato = contrato