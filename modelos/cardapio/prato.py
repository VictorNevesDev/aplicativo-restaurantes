from modelos.cardapio.item_cardapio import ItemCardapio

# Essa classe vai herdar métodos e atributos de uma outra classe, no caso a classe ItemCardapio
class Prato(ItemCardapio):

    # Método especial construtor que define 
    def __init__(self, nome, preco, descricao):

        # Objeto super() permite que você acesse informações da classe ItemCardapio
        super().__init__(nome, preco)
        self.descricao = descricao

    # Método especial que define a representação de string de um objeto
    def __str__(self):
            return self._nome
    

    def aplicar_desconto(self):
        self._preco -= self._preco * 0.05