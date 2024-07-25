
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Classe abstrata = Força as classes 'filhas' a obrigatoriamente terem esse método
    @abstractmethod
    def aplicar_desconto(self):
        pass
        