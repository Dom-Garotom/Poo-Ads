from ator import Ator
from contrato import Contrato

class Personagem (Ator):
    _caracterizacao : str
    _novela : str

    def __init__(self, nome : str , sexo : str, contrato : Contrato , novela : str,  caracterizacao : str) :
        super().__init__(nome, sexo, contrato)
        self._novela = novela
        self._caracterizacao = caracterizacao