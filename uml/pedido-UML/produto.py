class Produto:
    _codigo : int
    _valor : float
    _descricao : str

    def __init__(self , codigo : int  ,  valor : float , descricao : str ):
        self._codigo = codigo
        self._valor = valor
        self._descricao = descricao